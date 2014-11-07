import random
print "first move"
while (True):
	input1 = raw_input("What is your move? ")

	#if (input1 == 'r' or input1 == 'p' ):
	if input1 in ['r','p','s','R','P','S']:
		#then it's valid
		input1 = input1.upper()
		mylist=['R','P','S']
		comp_input=random.choice(mylist)
		print"comp move?"
		print comp_input
                if (input1==comp_input):
			print"play again"
			continue
		elif ((input1=='P' and comp_input=='R') or(input1=='S' and comp_input=='P') or (input1=='R' and comp_input=='S')):
			print"input1 won" #this means I win
			
		else: 
			print"losser:P" #this means computer wins
		
 			
		
	else:	
		print"wrong move"#it's not
		break
#here i'm done
