n,t,k,d=[int(i) for i in input().split()]
q=t
i1=q
i2=d
o=k
p=0
count=1
cum=1
while(o<n):
    o=o+k
    count=count+1
a=(count*t)
 
 
 
while(q<=d):
    if(q>=d):
        break
    else:
        q=q+t
        cum=cum+1
             
c=(cum*k)
if(c>=n):
    p=1
    
while(c<n):
    if(c>=n):
        break
    i2=i2+t
    c=c+k
    if(c>=n):
        break
    else:
        i1=i1+t
        c=c+k
e=max(i1,i2)
if(p>0):
    print("no")
else:
    if(e<a):
        print("yes")
                   
    else:
        print("no")
 
