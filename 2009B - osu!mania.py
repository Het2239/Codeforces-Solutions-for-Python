time= int(input())
for i in range(time):
    nl=list()
    st=''
    for j in range(int(input())):
        stl=input()
        sti=stl.index('#')
        sti=sti+1
        nl.append(sti)
    nll=nl[::-1]
    for k in nll:
        st+=f"{k} "
    print(st)
