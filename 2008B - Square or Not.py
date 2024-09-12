for c in range(int(input())):
    num=int(input())
    st=input()
    count=0
    order=0
    if(num==1 and st=='1'):
        print('Yes')
    
    elif((num%(num**0.5)==0)):
        order=int(num**0.5)
        for i in range(len(st)):
            if(st[i]=='0'):
                count+=1
        if(count==int(((num**0.5)-2)**2)):
            print('Yes')
        else:
            print('No')
    else:
        print('No')
