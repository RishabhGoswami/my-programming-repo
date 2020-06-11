s=str(input())
n=int(input())
for i in range(n):
    a=[str(i) for i in input().split()]
    if(a[0]==s and a[2]==s):
        if(int(a[1])>int(a[3])):
            print("Player 1 wins")
        elif(int(a[1])<int(a[3])):
            print('Player 2 wins')
        else:
            print('Draw')
    elif(a[0]==s or a[2]==s):
        if(a[0]==s):
            print('Player 1 wins')
        elif(a[2]==s):
            print('Player 2 wins')
        else:
            print("Draw")
    else:
        if(int(a[1])>int(a[3])):
            print("Player 1 wins")
        elif(int(a[1])<int(a[3])):
            print('Player 2 wins')
        else:
            print('Draw')
