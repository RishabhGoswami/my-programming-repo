a,b,c=[int(i) for i in input().split()]
d=[int(i) for i in input().split()]
e=[int(i) for i in input().split()]
l=[]
for i in range(0,len(d)):
    for j in range(0,len(e)):
        if((e[j]+d[i])>a):
            pass
        else:
            l.append(e[j]+d[i])
if(len(l)==0):
    print(-1)
else:
    print(max(l))
