#Given an integer,n, perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of to 2 to 5 , print Not Weird
#If n is even and in the inclusive range of to 6 to 20 , print Weird
#If n is even and greater than 20 , print Not Weird

#Input :

#A single line containing a positive integer,n .

if __name__ == '__main__':
    n = int(raw_input())
if(n % 2 != 0) :
    print("Weird")
elif (n in range (2, 6) and n % 2 == 0) :
    print("Not Weird")
elif (n in range (6, 21) and n % 2 == 0) :
    print("Weird")
else :
    print("Not Weird")




