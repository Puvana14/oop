s1={1,2,3,4,5,7}
s2={'a',9.7,8,'raj','oops'}
print("1)union\n2)intersection\n3)length\n4)symmetric diff\n5)pop an element\n6)copy\n7)issubset\n8)issuperset\n9)isdisjoint\n10)remove an element\n11)exit\n")
k=1
while(k==1):
	ch=int(input("enter your choice "))
	if(ch==1):
		print("union of  {} and {} is {}" .format(s1,s2,s1.union(s2)))
	elif(ch==2):
		print("intersection of {} and {} is {}" .format(s1,s2,s1.intersection(s2)))
	elif(ch==3):
		print("length of {} is {}" .format(s2,len(s2)))
	elif(ch==4):
		print("symmetric difference of {} and {} is {}" .format(s1,s2,s1.symmetric_difference(s2)))
	elif(ch==5):
		print("adding an element 9 to  {1,2,3,4,5,7} : {} " .format(s1,s1.add(9)))
	elif(ch==6):
		print("copy of {} : {}" .format(s1,s1.copy()))
	elif(ch==7):
		print("{} a subset of {} : {} " .format(s1,s2,s1.issubset(s2)))
	elif(ch==8):
		print("{} a superset of {} : {}" .format(s1,s2,s1.issuperset(s2)))
	elif(ch==9):
		print("{} and {} are disjoint: {}" .format(s1,s2,s1.isdisjoint(s2)))
	elif(ch==10):
		print("removing element 5 in {1,2,3,4,5,7}: {}" .format(s1))
	elif(ch==11):
		k=0
	else:
		print("invalid")

