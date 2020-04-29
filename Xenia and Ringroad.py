import math 
a,b=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
d=1
sum=0
for i in range(0,len(c)):
    if(c[i]==d):
        d=c[i]
        pass
    else:
        if(c[i]>d):
            e=abs(c[i]-d)
            d=c[i]
            sum=sum+e
        else:
            e=a-abs((c[i]-d))
            d=c[i]
            sum=sum+e
print(sum)  
