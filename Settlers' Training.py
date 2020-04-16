b=[int(i) for i in input().split()]
a=[int(i) for i in input().split()]
count=0
sums=sum(a)
while(sums<b[0]*b[1]):
    sums=sum(a)
    s=set()
    for i in range(0,len(a)):
        if(a[i] not in s):
            if(a[i]<b[1]):
                s.add(a[i])
                a[i]=a[i]+1
                
        else:
            continue
    count=count+1
if(count==0):
    print(0)
else:
    print(count-1)
