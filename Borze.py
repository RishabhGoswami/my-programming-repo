s=str(input())
d=''
i=0
# print(len(s))
while(i<len(s)):
    if(s[i]=="."):
        d=d+'0'
        i=i+1
#         print(d)
    elif(s[i]=='-' and s[i+1]=='-'):
        d=d+'2'
#         print(d)
        i=i+2
        
    elif(s[i]=='-' and s[i+1]=='.'):
        d=d+'1'
#         print(d)
        i=i+2     
print(d)  
