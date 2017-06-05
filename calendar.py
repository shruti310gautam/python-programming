#You are given a date. Your task is to find what the day is on that date.# Enter your code here. Read input from STDIN. Print output to STDOUT

import calendar
m,d,y = map(int,raw_input().split())
days = {0:"MONDAY",1:"TUESDAY",2:"WEDNESDAY",3:"THURSDAY",4:"FRIDAY",5:"SATURDAY",6:"SUNDAY"}
indx = calendar.weekday(y,m,d)
print(days[indx])

