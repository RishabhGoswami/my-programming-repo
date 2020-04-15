    n,m=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    sums=0
    l=[]
    g=[]
    for i in range(m):
        b,c=[int(i) for i in input().split()]
        l=a[b-1:c]
        c=set(l)
        for i in c:
            sums=sums+(i*l.count(i))
        if(sums<0):
            sums=0
        else:
            g.append(sums)
            sums=0
    print(sum(g))
