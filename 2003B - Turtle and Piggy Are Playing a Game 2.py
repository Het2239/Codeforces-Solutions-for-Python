for c in range(int(input())):
    num=int(input())
    st=input()
    nl=st.split()
    for i in range(len(nl)):
        nl[i]=int(nl[i])
    nl.sort()
    
    if(num==2):
        print(int(nl[1]))
    elif(num%2==0):
        
        print(int(nl[int((num/2))]))
    elif(num%2==1):
        print(int(nl[(int((num-1)/2))]))
