import math
a,b=[int(i) for i in input().split()]
c=abs((b-1)-a)
if(a<(b-1)):
    print("No")    
elif(b==0 and a>0):
    print("No")
elif(b==1 and a>0):
    print("No")
    
else:    
    if(c%2==0 and (b-1)<=a):
        print("Yes")
    else:
        print("No")
