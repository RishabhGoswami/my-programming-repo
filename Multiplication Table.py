a,b=[int(i) for i in input().split()]
count=0
for i in range(1,a+1):
    if(b%i==0 and i*a>=b):
        count=count+1
print(count)        
