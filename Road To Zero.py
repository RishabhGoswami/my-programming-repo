import math
n=int(input())
for i in range(n):
    x,y=[int(i) for i in input().split()]
    a,b=[int(i) for i in input().split()]    
    sum=0
    sums=0
    sum=sum+(x+y)*a
    d=min(x,y)
    if(d==x):
        sums=sums+(x*b)
        y=y-x
        sums=sums+(y*a)
    elif(d==y):
        sums=sums+(y*b)
        x=x-y
        sums=sums+(x*a)  
    print(min(sum,sums))
