import random

def thuvienten(n):
	temp=open('Data/Ho.txt','r')
	ho=temp.read()
	ho=ho.split()
	temp.close()

	temp=open('Data/Lot.txt','r')
	lot=temp.read()
	lot=lot.split()
	temp.close()

	temp=open('Data/Ten.txt','r')
	ten=temp.read()
	ten=ten.split()
	temp.close()

	dem=0
	list_name=[]
	while dem!=n:
		dem+=1
		random_t=random.randrange(len(ten))
		choose_ten=ten[random_t]

		random_t=random.randrange(len(lot))
		choose_lot=lot[random_t]

		random_t=random.randrange(len(ho))
		choose_ho=ho[random_t]

		full_name=' '.join([choose_ho,choose_lot,choose_ten])
		list_name.append(full_name)
	return list_name