    import math
    a,b=[int(i) for i in input().split()]
    f='abcdefghijklmnopqrstuvwxyz'
    s=f[0:b]
    d=math.floor(a/b)
    s=s*d
    e=abs(len(s)-a)
    s=s+f[0:e]
    print(s)
