s=str(input())
d=str(input())
a=sorted(s)
b=sorted(d)
c=set(b)
f=set(a)
di={}
sum=0
count=0
for i in c:
    if i in f:
        count=count+1
for   i  in c:
    if(b.count(i)<a.count(i)):
        di[i]=b.count(i)
    elif(b.count(i)>a.count(i)):
        di[i]=a.count(i)
    else:
        di[i]=a.count(i)
for k,v in di.items():
    sum=sum+v
if(sum==0 or count!=len(c)):
    print(-1)
else:
    print(sum)
