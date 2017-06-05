#You are given X,Y and Z three integers and representing the dimensions of a cuboid along with an integer N. You have to print a list of all possible coordinates given #by (i,j,k)on a 3D grid where the sum of i+j+k is not equal to N. Here, 0<=i<=X; 0<=j<=Y;  0<=k<=Z  

#Sample Input

#1
#1
#1
#2

if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])


#Sample Output= [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]] 

