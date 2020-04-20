n=int(input())
a=[int(i) for i in input().split()]
a=sorted(a,reverse=True)
count=0
sums=0
f=sum(a)
if(n==0):
    print(0)
elif(f<n):
    print(-1)
else:
    
    for i in range(0,len(a)):
        count=count+1
        sums=sums+a[i]
        if(sums==n or sums>n):
            print(count)
            break
