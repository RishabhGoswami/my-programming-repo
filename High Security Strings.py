s=str(input())
n=int(input())
d={'a':n}
sum=0
for i in range(0,len(s)):
    e=ord(s[i])-ord('a')
    f=n+e
    if(f>25):
        f=f-26
        sum=sum+f
    else:
        sum=sum+f
print(sum)
        
        
