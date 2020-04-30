n=int(input())
a=[int(i) for i in input().split()]
count=0
sums=0
for i in range(0,len(a)):
    if(a[i]%2!=0):
        count=count+1
if(count%2!=0):
    print("NO")
else:   
    while(count>0):
        for i in range(0,len(a)-1):
            if(a[i]%2!=0):
                a[i]=a[i]+1
                if(a[i+1]%2!=0):
                    a[i+1]=a[i+1]+1
                    count=count-2
                    sums=sums+2
                        
                else:
                    a[i+1]=a[i+1]+1
                    sums=sums+2
                
                
            
        
    

    print(sums)  
                
            
            
