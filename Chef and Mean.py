n=int(input())
for i in range(n):
    m=int(input())
    a=[int(i) for i in input().split()]
    b=sum(a)
    mean=b/m
    flag=0
    for i in range(0,len(a)):
        f=b-a[i]
        if(f/(m-1)==mean):
            flag=1
            v=i+1
            break
        else:
            pass
    if(flag>0):
        print(v)
    else:
        print('Impossible')
        
    
