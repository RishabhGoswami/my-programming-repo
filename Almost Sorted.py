s=int(input())
a=[int(i) for i in input().split()]
d=sorted(a)
l=[]
for i in range(0,len(d)):
    if(d[i]!=a[i]):
        l.append(i+1)
if(len(l)==2):
    print('yes')
    print('swap',l[0],l[1])
    
elif(len(l)>2):
    c=l[0]
    e=l[len(l)-1]
    f=a[c-1:e][::-1]
    g=a[0:c-1]+f+a[e:]
    if(g==d):
        print("yes")
        print('reverse',c,e) 
    else:
        print("no")
else:
    print("no")
