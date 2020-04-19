a,b=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
sums=0
count=0
l=[]
l1=[]
for i in range(0,len(c)):
    if(c[i]<0):
        l.append(c[i])
        count=count+1
    else:
        l1.append(c[i])
        sums=sums+c[i]       
if(count==0):
    s=sorted(c)
    if(b%2==0):
        pass
    else:
        s[0]=s[0]*(-1)
    print(sum(s))    
else:
    if(count==b ):
        s=sorted(c)
        for i in range(0,count):
            s[i]=s[i]*(-1)
        print(sum(s))    
    elif(b<count):
        s=sorted(c)
        for i in range(0,b):
            s[i]=s[i]*(-1)
        print(sum(s))    
    else:
        g=b-count
        for i in range(0,len(l)):
            l[i]=l[i]*(-1)
        v=l+l1
        z=sorted(v)
        if(g%2==0):
            pass
        else:
            z[0]=(z[0]*((-1)**(b-count)))
        print(sum(z))    
