# for gcd of 3 nos. in 3 pairs of 2 to be equal to 1 we should select 3 consecutive numbers starting with an odd number 
# therefore each pair will contain two odd nos and the answer will be total no of odd numbers by 2 rounded.

nl=list()
for c in range(int(input())):
    count=0
    ocount=0
    l,r=map(int,input().split())
    # rand=set(range(l,r+1))
    # if(len(rand)<3):
    #     break
    
    # for i in list(rand):
    #     if(i%2==1):
    #         ocount+=1
    # count=ocount//2
    count=(((r+1)//2-l//2)//2)
    print(count)
 
    
        
    
    
        
    


