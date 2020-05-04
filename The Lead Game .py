n=int(input())
sums=0
sumss=0
max=0
ans=0
for i in range(n):
    a,b=[int(i) for i in input().split()]
    sums=sums+a
    sumss=sumss+b
    if(sums>sumss):
        d=sums-sumss
        if(d>max):
            max=d
            ans=1

    elif(sumss>sums):
        d=sumss-sums
        if(d>max):
            max=d
            ans=2
    else:
        pass
print(ans,max)
    
