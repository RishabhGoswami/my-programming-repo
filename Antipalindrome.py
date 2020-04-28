s=str(input())
if(s!=s[::-1]):
    print(len(s))
else:
    
    flag=0
    for i in range(1,len(s)):
        d=s[i:]
        if(d!=d[::-1]):
            flag=1
            break
        else:
            pass
    if(flag>0):
        print(len(s)-i)
    else:
        print(0)
