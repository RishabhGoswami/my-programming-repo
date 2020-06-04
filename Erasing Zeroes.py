# erasing zeroes
n=int(input())
for i in range(n):
    l=[]
    d=0
    s=str(input())
    for j in range(0,len(s)):
        if(s[j]=='1'):
            l.append(j)
    if(len(l)==0 or len(l)==1):
        print(0)
    else:
        for j in range(0,len(l)-1):
            d=d+((l[j+1]-l[j])-1)
        print(d)  
