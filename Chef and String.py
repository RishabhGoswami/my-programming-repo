n=int(input())
for  i in range(n):
    s=str(input())
    j=0
    c=0
    if(len(s)==1):
        print(0)
    else:    
        while(j<=len(s)):
            if(s[j]==s[j+1]):
                j=j+1
                pass
            else:
                c=c+1
                j=j+2
            if(j>=len(s)-1):
                break
        print(c)            
