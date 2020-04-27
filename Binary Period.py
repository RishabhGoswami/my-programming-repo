n=int(input())
for i in range(n):
    s=str(input())
    c=set(s)
    if(len(c)==1):
        print(s)
    else:
        d=s.count('1')
        e=s.count('0')
        f=s[0]
        for i in range(0,len(s)-1):
            if(s[i]==s[i+1] and s[i]=='0'):
                f=f+'1'+s[i+1]
            elif(s[i]==s[i+1] and s[i]=='1'):
                f=f+'0'+s[i+1]
            else:
                f=f+s[i+1]
        print(f)
