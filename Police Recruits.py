    a=int(input())
    b=[int(i) for i in input().split()]
    csum=0
    sum=0
    for i in range(0,len(b)):
        if(b[i]>0):
            sum=sum+b[i]
        elif(b[i]<0):
            csum=csum+1
            if(sum>0):
                csum=csum-1
                sum=sum-1
            else:
                continue
    print(csum)  
