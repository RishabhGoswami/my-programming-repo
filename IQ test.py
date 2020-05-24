n=int(input())
a=[int(i) for i in input().split()]
a=a[::-1]
s=0
c=0
for i in range(0,len(a)):
    if(a[i]%2==0):
        s=s+1
    else:
        c=c+1
# print(s,c)        
if(c==1):
    for i in range(0,len(a)):
        if(a[i]%2!=0):
            d=i+1
            break
 
    print((n-d)+1)    
else:
    for i in range(0,len(a)):
        if(a[i]%2==0):
            d=i+1
            break
 
    print((n-d)+1)        
        
