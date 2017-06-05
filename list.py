#Consider a list (list = []). You can perform the following commands:

#    insert i e: Insert integer e at position i.
#    print: Print the list.
#    remove e: Delete the first occurrence of integer e .
#    append e: Insert integer e at the end of the list.
#    sort: Sort the list.
#    pop: Pop the last element from the list.
#    reverse: Reverse the list.

#Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in #order #and perform the corresponding operation on your list.

if __name__ == '__main__':
    N = int(raw_input())
    l = []
    l.insert(0,5)
    l.insert(1,10)
    l.insert(0,6)
    print(l)
    l.remove(6)
    l.append(9)
    l.append(1)
    l.sort()
    print(l)
    temp = l.pop()
    l.reverse()
    print(l)

#Sample Input

#12
#insert 0 5
#insert 1 10
#insert 0 6
#print 
#remove 6
#append 9
#append 1
#sort 
#print
#pop
#reverse
#print

#Sample Output

#[6, 5, 10]
#[1, 5, 9, 10]
#[9, 5, 1]

