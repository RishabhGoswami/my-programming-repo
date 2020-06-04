#hey stalker
n,m=[int(i) for i in input().split()]
l=[]
a=[]
for i in range(m):
    g,h=[str(i) for i in input().split()]
    l.append(g)
    a.append(h)
# print(l,a)
s=str(input())
s=s.split(' ')
z=[]
for i in range(0,len(s)):
    d=s[i]
#     print(d)
    if(d in l):
        f=l.index(d)
        if(len(l[f])>len(a[f])):
            z.append(a[f])
            
        elif(len(l[f])<len(a[f])):
             z.append(l[f])
        else:
            z.append(l[f])
    elif(d in a):
        f=l.index(d)
        if(len(l[f])>len(a[f])):
            z.append(a[f])
            
        elif(len(l[f])<len(a[f])):
             z.append(l[f])
        else:
            z.append(l[f])
print(*z)
