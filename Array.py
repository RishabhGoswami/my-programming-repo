n=int(input())
a=[int(i) for i in input().split()]
l=[]
b=[]
c=[]
d=[]
s=[]
for i in range(0,len(a)):
    if(a[i]<0):
        l.append(a[i])
for i in range(0,len(a)):
    if(a[i]>0):
        s.append(a[i]) 
if(len(l)%2!=0):
    d.append(0)
    a.remove(0)
    b.append(l[0])
    l.remove(l[0])
    c=c+l
    c=c+s
elif(len(l)%2==0):
    d.append(0)
    a.remove(0)
    d.append(l[0])
    l.remove(l[0])
    b.append(l[0])
    l.remove(l[0])
    c=c+s
    c=c+l
b.insert(0,len(b))
c.insert(0,len(c))
d.insert(0,len(d))
print(*b)
print(*c)
print(*d)
