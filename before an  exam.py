a,b=[int(i) for i in input().split()]
l=[]
g=[]
for i in range(a):
    c,d=[int(i) for i in input().split()]
    l.append(c)
    g.append(d)
e=sum(l)
f=sum(g)
for i in range(0,len(l)):
    if(c==b):
        break
    c=sum(l)
    if(l[i]==g[i]):
        continue
    else:
        while(l[i]<g[i] ):
            l[i]=l[i]+1
            c=c+1
            if(c==b):
                break
if(b>f or b<e):
    print("NO")
else:
    print("YES")
    print(*l)
