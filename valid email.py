#You are given an integer N followed by N email addresses. Your task is to print a list containing only valid email addresses in lexicographical order.

import re
def fun(s):
    # return True if s is a valid email, else return False
    a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
    return(a)

