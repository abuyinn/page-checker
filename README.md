# page-checker

This is simple program to check if website page have changed.


### Requirements
#### Linux

This program was tested on Linux.

1. Python3.
2. BeautifulSoup.
3. mpg123 (to play mp3).
4. MP3 file with name "aa.mp3" in the same directory.

#### Windows

Not tested.

Probably will work if you change (or delete) command `os.system(...`


### Running
```
python3 checker.py [--url-- [--delay-- [--id-- [--class--]]]]
```

`--url--` is an URL to check.

`--delay--` is time to delay in seconds.

`--id--` is an id in HTML to check.

`--class--` is a class in HTML to check.

If you use `--id--` or `--class--`, the program will check only these things.
Otherwise will check the whole page.

