time=int(input())
sum=list()
for c in range(time):
    muns=int(input())
    n=input()
    numl=n.split(' ')
    ne=list()
    no=list()
    se=0
    so=0
    for i in range(len(numl)):
        if(i%2==0):
            ne.append(numl[i])
        elif(i%2==1):
            no.append(numl[i])
    for j in ne:
        se+=int(j)
    for k in no:
        so+=int(k)
    sum.append(se-so)
for i in sum:
    print(i)
