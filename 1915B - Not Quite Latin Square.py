a=int(input())
lis = list()
i=0
while(i<a):
    l1=input()
    l2=input()
    l3=input()

    mark1=l1.find("?")
    mark2=l2.find("?")
    mark3=l3.find("?")
    if(mark1>=0):
        mark=l1.find("A")
        if(mark== -1):
            lis.append("A")
        mark=l1.find("B")
        if(mark== -1):
            lis.append("B")
        mark=l1.find("C")
        if(mark== -1):
            lis.append("C")
    if(mark2>=0):
        mark=l2.find("A")
        if(mark== -1):
            lis.append("A")
        mark=l2.find("B")
        if(mark== -1):
            lis.append("B")
        mark=l2.find("C")
        if(mark== -1):
            lis.append("C")
    if(mark3>=0):
        mark=l3.find("A")
        if(mark== -1):
            lis.append("A")
        mark=l3.find("B")
        if(mark== -1):
            lis.append("B")
        mark=l3.find("C")
        if(mark== -1):
            lis.append("C")
    i+=1
h=0
while(h<a):
    print(lis[h])
    h+=1
