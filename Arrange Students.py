n=int(input())
for i in range(n):
    a=int(input())
    b=[int(i) for i in input().split()]
    c=[int(i) for i in input().split()]
    d=''
    s=''
    l=[]
    flag=0
    count=0
    for j in range(0,len(b)):
        e=min(b)
        f=min(c)
        if(e<f):
            l.append(e)
            l.append(f)
            s=s+'B'+'G'
            d=d+'B'+'G'
            b.remove(e)
            c.remove(f)
        elif(f<e):
            l.append(f)
            l.append(e)
            s=s+'G'+'B'
            d=d+'G'+'B'
            b.remove(e)
            c.remove(f)
        else:
            l.append(f)
            l.append(e)
            s=s+'G'+'B'
            d=d+'B'+'G'
            b.remove(e)
            c.remove(f)
    for j in range(0,len(l)-1):
        if(l[j]<=l[j+1]):
            pass
        else:
            flag=1
            break
# print(l,s,d)        
    for j in range(0,len(s)-1):
        if(s[j]!=s[j+1]):
            pass
        else:
            count=count+1
            break
    for j in range(0,len(d)-1):
        if(d[j]!=d[j+1]):
            pass
        else:
            count=count+1
            break
    if(flag>0 or count==2):
        print("NO")
    else:
        print("YES")
