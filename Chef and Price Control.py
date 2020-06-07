import math
n=int(input())
for i in range(n):
    m,k=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    c=0
    for i in range(0,len(a)):
        if(a[i]>k):
            c=c+abs(a[i]-k)
    print(c)   
