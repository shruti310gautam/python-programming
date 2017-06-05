#You are given a string S .
#Your task is to find out whether S is a valid regex or not.


import re
for i in range (int(raw_input())):
    try:
        if re.compile(raw_input()):
            print "True"
    except:
        print "False"
