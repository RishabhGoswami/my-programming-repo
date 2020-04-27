n=int(input())
sum=0
for i in range(n):
    s=str(input())
    if(s[0]=="T"):
        sum=sum+4
    if(s[0]=="C"):
        sum=sum+6
    if(s[0]=="O"):
        sum=sum+8
    if(s[0]=="D"):
        sum=sum+12
    if(s[0]=="I"):
        
        sum=sum+20    
print(sum)
