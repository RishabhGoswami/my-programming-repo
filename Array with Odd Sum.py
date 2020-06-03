n=int(input())
for i in range(n):
    a=int(input())
    b=[int(i) for i in input().split()]
    c=0
    for j in range(0,len(b)):
        if(b[j]%2!=0):
            c=c+1
    d=len(b)-c        
    if(c%2!=0):
        print("Yes")
    else:
        if(c>0 and d>0):
            print("Yes")
        else:
            print("No")
