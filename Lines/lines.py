#!/usr/bin/env python
#usage: lines.py filenames seperated by space
#my personal way of using it: lines.py `git diff --no-ext-diff --name-only HEAD~1 HEAD | grep .py`

import sys 

TAB_WIDTH = 8 
LINE_LENGTH = 79

def count(line):
        length = 0 
        for i in line:
                if i == "\n":
                        continue
                if i == "\t":
                        length+=TAB_WIDTH
                else:
                        length+=1
        return length

def check_file(filename):
        f = open(filename, "r")
        linecount = 1 
        docstring_dq = False
        docstring_sq = False
        for line in f.readlines():
                if "\"\"\"" in line:
                        docstring_dq = not docstring_dq
                if "'''" in line:
                        docstring_sq = not docstring_sq

                if docstring_dq or docstring_sq:
                        linecount+=1
                        continue

                curr_line = count(line)
                if curr_line > LINE_LENGTH:
                        print "Exceeded by %d chars:%s:%d" % ( 
                                        abs(LINE_LENGTH-curr_line),
                                        filename,
                                        linecount)
                linecount+=1

if __name__ == "__main__":
        if len(sys.argv) < 2:
                print "You need to supply a command line argument"
                sys.exit(1)
        else:
                files = sys.argv[1:]
                for file in files:
                        check_file(file)