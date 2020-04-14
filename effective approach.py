n=int(input())
a=[int(i) for i in input().split()]
m=int(input())
b=[int(i) for i in input().split()]
sums=0
dum=0
d={}
for i,x in enumerate(a):
    d[x]=i+1
for s in range(m):
    sums=sums+d.get(b[s])
    dum=dum+len(a)-d.get(b[s])+1
print(sums,dum)     
