n=int(input())
l=[]
for i in range(n):
    s=str(input())
    l.append(s)
c=0
d=0
m=[]
n=[]
for i in range(0,len(l)):
    if(l[i]=='Heads'):
        c=c+1
    elif(l[i]!='Heads'):
        m.append(c)
        c=0
for i in range(0,len(l)):
    if(l[i]=='Tails'):
        d=d+1
    elif(l[i]!='Tails'):
        n.append(d)
        d=0
if(d>0 ):
    n.append(d)
if(c>0 ):
    m.append(c)
# print(m,n)
if(len(n)==0):
    v=0
elif(len(n)>0):
    v=max(n)
if(len(m)==0):
    k=0
elif(len(m)>0):
    k=max(m)
print(k,v)
