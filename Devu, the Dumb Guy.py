    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    c=sorted(b)
    count=0
    d=a[1]
    for i in range(0,len(c)):
        count=count+(d*c[i])
        if(d>1):
            d=d-1
        else:
            continue
    print(count)        
