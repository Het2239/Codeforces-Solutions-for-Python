time=int(input())
nl=list()
i=0
while(i<time):
    num=input()
    sum =int(num[0])+int(num[1])
    nl.append(sum)
    i+=1
h=0
while(h<time):
    print(nl[h])
    h+=1
