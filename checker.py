#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import time
import os
import sys


########
# CONSTS
########

debug          = False
n_chars_in_row = 40


##########
# DEFAULTS
##########

d_url          = "http://127.0.0.1/"
d_delay_in_sec = 10
d_html_id      = ""
d_html_class   = ""


####################################
# FUNCTIONS TO GET AND PARSE WEBPAGE
####################################

def get_id(_soup, _id_name):
    return _soup.find(id=_id_name)


def get_class(_soup, _class_name):
    return _soup.find_all(class_=_class_name)


def get_soup(_url):
    r = requests.get(_url)
    r_html = r.text
    soup = BeautifulSoup(r_html, "lxml")
    return soup



##################
# USEFUL FUNCTIONS
##################

# print only in debug mode
def print_debug(to_print):
    if debug:
        print(to_print)


def get_args():
    if len(sys.argv) == 1:
        print("Usage: python3 checker.py [--url-- [--delay-- [--id-- [--class--]]]]")

    _url          =       sys.argv[1]  if len(sys.argv) > 1 else d_url
    _delay_in_sec = float(sys.argv[2]) if len(sys.argv) > 2 else d_delay_in_sec
    _html_id      =       sys.argv[3]  if len(sys.argv) > 3 else d_html_id
    _html_class   =       sys.argv[4]  if len(sys.argv) > 4 else d_html_class

    return (_url, _delay_in_sec, _html_id, _html_class)


def print_args(_url, _delay_in_sec, _html_id, _html_class):
    print("\nParameters:")
    print("  URL       :",  _url)
    print("  Delay [s] :",  _delay_in_sec)
    print("  HTML id   :",  _html_id)
    print("  HTML class:",  _html_class)
    print("\n")


# pattern is this thing to compare:
#       full page
#   or  element with some id and elements with some class
def get_pattern(_url, _html_id, _html_class, isFirstAttempt):
    try:
        soup = get_soup(_url)
    except:
        # connection problem
        if isFirstAttempt:
            print("Error: Connection problem.")
            sys.exit(1)
        else:
            return None

    if _html_id == "" and _html_class=="":
        return soup     # full page
    else:
        print_debug( [get_id(soup, _html_id),get_class(soup, _html_class)])
        return       [get_id(soup, _html_id),get_class(soup, _html_class)]


def changed():
    print("\n\nNew version available!\nCheck it.\n\n")
    os.system("mpg123 aa.mp3")
    answer = input("Continue? (enter / n):")
    if len(answer)>0 and (answer[0]=='n' or answer[0]=='N'):
        print("Exiting...")
        sys.exit(0)



######
# MAIN
######
if __name__=="__main__":

    # Arguments: get and print
    url, delay_in_sec, html_id, html_class = get_args()
    print_args(url, delay_in_sec, html_id, html_class)

    # Get first version
    pattern = get_pattern(url, html_id, html_class, True)
    print_debug(pattern)
    print("Got it!")

    while True:
        for it in range(n_chars_in_row):
            print(".", end=("\n" if it==n_chars_in_row-1 else ""), flush=True)

            time.sleep(delay_in_sec)

            new_pattern = get_pattern(url,html_id, html_class, False)

            if new_pattern == None:
                print("\tError: Connection problem.")
                break
            if pattern != new_pattern:
                changed()
                pattern = new_pattern
                break
            else:
                print_debug("\tThe same...")


