for c in range(int(input())):
    a,b=map(int, input().split())
    if(a==0):
        if(b%2==0):
            print('YES')
        else:
            print("NO")
    elif(((b*2)+a)%2==0):
        print("YES")
    else:
        print('NO')
