n=int(input())
s=str(input())
d=0
sum=0
l=[]
for i in range(0,len(s)):
    if(s[i]!='x'):
        if(d>=3):
            l.append(d)
        d=0
    else:
        d=d+1
        
if(i==len(s)-1 and d>=3):
    l.append(d)
# print(l)    
for i in range(0,len(l)):
    sum=sum+(l[i]-2)
print(sum) 
