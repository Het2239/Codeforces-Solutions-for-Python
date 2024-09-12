# You are given three digits a b c Two of them are equal, but the third one is different from the other two. Find the value that occurs exactly once.
time=int(input())
nl=list()
i=0

while(i<time):
    num=input()
    c1=num.count(num[0])
    c2=num.count(num[2])
    if(c1>1):
        if(num[0]==num[2]):
            nl.append(num[4])
        elif(num[0]==num[4]):
            nl.append(num[2])
    elif(c2>1):
        if(num[2]==num[0]):
            nl.append(num[4])
        elif(num[2]==num[4]):
            nl.append(num[0])
    i+=1

h=0
while(h<time):
    print(nl[h])
    h+=1
   
