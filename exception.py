#You are given two values a and b .
#Perform integer division and print a/b .

# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range (int(input())):
   
    try:
        a,b = map(int,raw_input().split())
        print (int(a)/int(b))
    except ZeroDivisionError as e:
        print "Error Code:",e
    except ValueError as v:
        print "Error Code:",v 
