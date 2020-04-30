t=int(input())
for i in range(t):
    count=0
    nk=input().split()
    n=int(nk[0])
    k=int(nk[1])
    a=[int(i) for i in input().split()]
    for i in range(0,n):
        if (a[i]<=0):
            count=count+1
        else:
            continue    
    if (count>=k):
        print("NO")
    else:
        print("YES")    


