m,n=[int(i) for i in input().split()]
a=max(n,m)
b=min(m,n)
sums=a*(b//2)
if(b%2!=0):
    sums=sums+a//2
print(sums)
