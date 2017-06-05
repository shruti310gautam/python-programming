#You are given N numbers. Store them in a list and find the second largest number. 

#Sample Input
#5
#2 3 6 6 5

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    print sorted(list(set(arr)))[-2]


#Sample Output=5

