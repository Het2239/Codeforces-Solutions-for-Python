# Program to find most frequent 
# element in a list
def most_frequent(List):
	counter = 0
	num = List[0]
	
	for i in List:
		curr_frequency = List.count(i)
		if(curr_frequency> counter):
			counter = curr_frequency
			num = i

	return num



for c in range(int(input())):
    time=int(input())
	
    st=input()
    count=0
    nl=st.split(' ')
    maxrep=most_frequent(nl)
    for i in nl:
	    if(i==maxrep):
	    	count+=1
    print(time-count)
