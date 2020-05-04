n=int(input())
v='aeiou'
for i in range(n):
    count=0
    m=int(input())
    s=str(input())
    for i in range(0,len(s)-1):
        if(s[i] not in v and s[i+1] in v):
            count=count+1
        else:
            pass
    print(count)    
            
