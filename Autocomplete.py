s=str(input())
a=int(input())
l=[]
for i in range(a):
    d=str(input())
    if(d.find(s)==0):
        l.append(d)
    else:
        pass  
if(len(l)>0):    
    min=l[0]    
    for i in range(1,len(l)):
        if(l[i]<min):
            min=l[i]
        else:
            continue
    print(min)        
else:
    print(s)
