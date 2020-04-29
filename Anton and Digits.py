a,b,c,d=[int(i) for i in input().split()]
e=min(min(a,c),d)
sum=0
sum=sum+(e*256)
a=a-e
f=min(a,b)
sum=sum+(f*32)
print(sum)
