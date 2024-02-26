print("1)list operations\n2)sets operation\n")
choice=int(input("enter the choice"))
if(choice==1):
	print("1)concat\n2)repeat factor\n3)length\n4)slicling\n5)reverse\n6)max\n7)count\n8)sum\n9)append\n10)extend\n11)exit\n")
	l1=[1,2,3,4,5,2]
	l2=['a',9.7,7,'raj','oops',7]
	k=1
	while(k==1):
		ch=int(input("enter your choice "))
		if(ch==1):
			print("concatenation of {} and {} is {}" .format(l1,l2,l1+l2))
		elif(ch==2):
			print("repeat factor of 2*{} is {}" .format(l1,2*l1))
		elif(ch==3):
			print("length of {} is {}" .format(l2,len(l2)))
		elif(ch==4):
			print("slicing of {} with start index-1 and end index-3  is {}" .format(l2,l2[1:3]))
		elif(ch==5):
			print("reverse of {} is {}" .format(l2,l2[::-1]))
		elif(ch==6):
			print("max of {} is {}" .format(l1,max(l1)))
		elif(ch==7):
			print("copy of {} is {}" .format(l2,l2.copy()))
		elif(ch==8):
			print("sum of elements of {} is {}" .format(l1,sum(l1)))
		elif(ch==9):
			print("appending 6 to {}" .format(l1,l1.append(6)))
		elif(ch==10):
			print("extending l1 with l2 gives {}" .format(l1,l2,l1.extend(l2)))
		elif(ch==11):
			k=0
		else:
			print("invalid")

else:
	s1={1,2,3,4,5}
	s2={'a',9.7,7,'raj','oops',7}
	print("1)union\n2)intersection\n3)length\n4)symmetric diff\n5)pop an element\n6)copy\n7)issubset\n8)issuperset\n9)isdisjoint\n10)remove an element\n11)exit\n")
	k=1
	while(k==1):
                ch=int(input("enter your choice "))
                if(ch==1):
                        print("union of  {} and {} is {}" .format(s1,s2,s1.union(s2)))
                elif(ch==2):
                        print("intersection of {} is {}" .format(s1,s2,s1.intersection(s2)))
                elif(ch==3):
        p                print("length of {} is {}" .format(s2,len(s2)))
                elif(ch==4):
                        print("symmetric difference of {} and {} is {}" .format(s1,s2,s1.symmetric_difference(s2)))
                elif(ch==5):
			print(s1.pop())
                elif(ch==6):
                        print("copy of s1 to s3 is {}" .format(s1.copy(s2))
                elif(ch==7):
                        print("{} a subset of {} : {} " .format(s1,s2,s1.issubset(s2)))
                elif(ch==8):
                        print("{} a superset of {} : {}" .format(s1,s2,s1.superset(s2)))
                elif(ch==9):
                        print("{} and {} are disjointsets " .format(s1,s2,s1.isdisjoint(s2)))
                elif(ch==10):
                        print("removing element 7 in {} gives {}" .format(s2,s2.remove(7)))
                elif(ch==11):
                        k=0
                else:
                        print("invalid")

