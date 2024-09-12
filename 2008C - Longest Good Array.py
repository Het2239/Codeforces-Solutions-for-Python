# for c in range(int(input())):
    
#     st=input()
#     nul=st.split(" ")
#     l=int(nul[0])
#     r=int(nul[1])
#     nl=[l]
    
#     while(nl[len(nl)-1]<r):
#         k=len(nl)
#         nl.append(nl[k-1]+k)
#     if(nl[len(nl)-1]>r):
#         nl.remove(nl[len(nl)-1])
#     print(len(nl))


# above good but takes more time

for k in range(int(input())): 
    a, b = map(int, input().split())
    i = 0
    while a + i <= b:
        a += i
        i += 1
    print(i)

# right solution but python takes longer time
# use pypy to successfully run the above program
