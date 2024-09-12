repeat = int(input())
i=0
nl=list()
while(i<repeat):
    data=input()
    time=data.split(":")
    if(int(time[0])>12 and int(time[0])<22):
        t=int(time[0])
        t= t-12
        nl.append(f"0{t}:{time[1]} PM")
    elif(int(time[0])>=22):
        t2=int(time[0])
        t2= t2-12
        nl.append(f"{t2}:{time[1]} PM")
    elif(time[0]=="00"):
        nl.append(f"12:{time[1]} AM")
    elif(int(time[0])<12):
        nl.append(f"{data} AM")
    elif(int(time[0])==12):
        nl.append(f"{data} PM")
    
    i+=1

h=0
while(h<repeat):
    print(nl[h])
    h+=1
