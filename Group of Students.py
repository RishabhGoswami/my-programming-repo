n=int(input())
l=[int(i) for i in input().split()]
b,c=[int(i) for i in input().split()]
g=0
for i in range(1,len(l)):
    d=l[0:i]
    e=l[i:]
    q=sum(d)
    w=sum(e)
    if(q in range(b,c+1) and w in range(b,c+1)):
        print(i+1)
        break
    else:
        g=g+1    
if(g==len(l)-1):
    print(0)
