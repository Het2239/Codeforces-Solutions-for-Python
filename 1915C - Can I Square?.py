time=int(input())
nl=list()
i=0
while(i<time):
    btime=input()
    sum=0
    cubes=input()
    num=cubes.split(" ")
    for val in num:
        
        sum+=int(val)
     
    sqrt_sum = int(sum**0.5)  
    if sqrt_sum**2==sum:  
        nl.append("YES")
    else:  
        nl.append("NO")
    i+=1

h=0
while(h<time):
    print(nl[h])
    h+=1

