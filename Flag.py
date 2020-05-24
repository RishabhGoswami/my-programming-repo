n,m=[int(i) for i in input().split()]
d=''
flag=0
for i in range(n):
    s=str(input())
    if(i==0 and len(set(s))==1):
        d=d+s[0]
    elif(len(set(s))>1):
        flag=1
#         break
    else:
        d=d+s[0]
        if(d[len(d)-1]==d[len(d)-2]):
            flag=1
#             break
if(flag>0):
    print("NO")
else:
    print("YES")
