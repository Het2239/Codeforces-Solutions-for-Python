# here we need minimum distance of k after which colours can repeat
# we need a max K*k colour set for the whole grid

for i in range(int(input())):
    n,m,k=map(int,input().split())
    ans=1

    if n<k : ans*=n
    else : ans*=k

    if m<k : ans*=m
    else : ans*=k

    print(ans)
