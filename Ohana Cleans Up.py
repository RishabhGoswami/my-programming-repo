n=int(input())
min=-1
l=[]
for i in range(n):
    s=str(input())
    l.append(s)
for i in  range(0,len(l)):
    if(l.count(l[i])>min):
        min=l.count(l[i])
print(min)        
