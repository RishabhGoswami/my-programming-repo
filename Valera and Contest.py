n,k,l,r,s,s1=[int(i) for i in input().split()]
l2=[]
l1=[]
c=int(s1//k)
while(len(l1)<k):
    l1.append(c)  
d=sum(l1)
if(d==s1):
    pass
else:  
    while(d<s1):
        for i in range(0,len(l1)):
            l1[i]=l1[i]+1
            d=d+1
            if(d==s1):
                break          
le=n-k 
while(len(l2)<le):
     l2.append(l)
e=sum(l2)
if(e==(s-s1)):
        pass
else:
    while(e<(s-s1)):
         for i in range(0,len(l2)):
                l2[i]=l2[i]+1
                e=e+1
                if(e==(s-s1)):
                    break
print(*(l1+l2)
