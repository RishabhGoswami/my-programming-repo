n=int(input())
for i in range(n):
    m=int(input())
    b=0
    c=0
    flag=0
    a=[int(i) for i in input().split()]
    for j in range(0,len(a)):
        if(a[j]==5):
            b=b+1
        elif(a[j]==10):
            if(b>0):
                b=b-1
                c=c+1
    
            else:
                flag=1
                break
                
        else:
            if(c>0 ):
                c=c-1 
#                 b=b+1
            elif(b>=2):
                b=b-2
                b=b+1
            else:
                flag=1
                break
            
    if(flag>0):
        print('NO')
    else:
        print("YES")
