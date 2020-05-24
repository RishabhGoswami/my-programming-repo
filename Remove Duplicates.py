n=int(input())
a=[int(i) for i in input().split()]
d=set()
a=a[::-1]
l=[]
for i in range(0,len(a)):
    if(a[i] in d):
        pass
    else:
        l.append(a[i])
        d.add(a[i])
#     print(l)    
        
print(len(l))
print(*l[::-1])
        
