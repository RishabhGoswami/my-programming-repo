    import  math
    a,b,c=[int(i) for i   in input().split()]
    d=(abs(a)-0)+(abs(b)-0)
    if(d%2==0):
        if(c>=d and c%2==0):
            print("Yes")
        else:
            print("No")
    else:
        if(c>=d and c%2!=0):
            print("Yes")
        else:
            print("No")
