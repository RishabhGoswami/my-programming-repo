n=int(input())
s=[int(i) for i in input().split()]
m=int(input())
d={}
k=0
for i in range(0,len(s)):
    d[i+1]=s[i]
for i in range(m):
    a,b=[int(i) for i in input().split()]
    if(n==1):
        k=1
        break
    if(a!=1 and a!=n):
        c=d[a-1]
        c=c+(b-1)
        d[a-1]=c
        d[a]=d[a]-b
        e=d[a+1]
        e=e+(d[a])
        d[a+1]=e
        d[a]=0
    if(a==1):
        d[a]=d[a]-b
        e=d[a+1]
        e=e+(d[a])
        d[a+1]=e
        d[a]=d[a]-d[a]  
    if(a==n):
        c=d[a-1]
        c=c+(b-1)
        d[a-1]=c
        d[a]=0
if(k>0):
    print(0)
else:    
    for i,j in d.items():
        print(j)
