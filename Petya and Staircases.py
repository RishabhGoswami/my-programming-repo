a,b=[int(i) for i in input().split()]
flag=0
if(b==0):
    print("YES")
else:        
    c=[int(i) for i in input().split()]
    d=sorted(c)
    if(1 in d or a in d):
        flag=1    
    elif(len(d)>=3):
        for i in range(0,len(d)-2):
            if((d[i+1]-d[i])==1 and (d[i+2]-d[i+1])==1):
                flag=1
            
    if(flag==1):
        print("NO")
    else:
        print("YES")
