n=int(input())
a=[int(i) for i in input().split()]
l=[a[0],a[len(a)-1]]
for i in range(1,len(a)-1):
    l.append(max(a[i],a[i+1]))
print(min(l))    
