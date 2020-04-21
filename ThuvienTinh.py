import random

def thuvientinh(n):
	temp=open('Data/tinhthanh.txt','r')
	tinh=temp.read()
	tinh=tinh.split('\n')
	temp.close()
	dem=0
	list_name=[]
	while dem!=n:
		dem+=1
		random_t=random.randrange(len(tinh))
		choose_tinh=tinh[random_t]
		list_name.append(choose_tinh)
	return list_name