n=int(input())
for i in range(n):
    l=[]
    min=-10**9
    a,b=[int(i) for i in input().split()]
    for i in range(a):
        c,d,e=[int(i) for i in input().split()]
        if(e<=b and (c*d)>min):
            min=c*d
    if(min>0):
        print(min)
    else:
        print("no tablet")
        
            
