a,b=[int(i) for i in input().split()]
c=[int(i) for i in input().split()]
l=[]
for i in range(0,len(c)-1):
    if(c[i]==c[i+1]):
        l.append(i)
if(len(l)==0):
    print(a)
elif(len(l)==1):
    print(max((l[0]+1),a-l[0]-1))
else:
    g=l[0]+1
    e=a-l[len(l)-1]-1
    h=-10**9
    for i in range(1,len(l)):
        i=l[i]-l[i-1]
        if(i>h):
            h=i    
    print(max(max(g,e),h)) 
