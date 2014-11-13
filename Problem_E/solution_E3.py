import random
print "first move"
mycount=0;
comp_count=0;
while (True):
	input1 = raw_input("What is your move? ")
	
	#if (input1 == 'r' or input1 == 'p' ):
	if input1 in ['r','p','s','l','k','R','P','S','L','K']:
		#then it's valid
		input1 = input1.upper()
		mylist=['R','P','S','L','K']
		comp_input=random.choice(mylist)
		print"comp move?"
		print comp_input
                if (input1==comp_input):
			print"play again"
			continue
		elif ((input1=='S' and comp_input=='P') or \
                      (input1=='P' and comp_input=='R') or \
		      (input1=='R' and comp_input=='L') or \
		      (input1=='L' and comp_input=='K') or \
		      (input1=='K' and comp_input=='S') or \
		      (input1=='S' and comp_input=='L') or \
		      (input1=='L' and comp_input=='P') or \
		      (input1=='P' and comp_input=='K') or \
		      (input1=='K' and comp_input=='R') or \
		      (input1=='R' and comp_input=='S')):
			print"input1 won" #this means I win
			mycount=1+mycount
		else: 
			print"loser:P" #this means computer wins
			comp_count=1+comp_count
 			
		
	else:	
		print"wrong move"#it's not
		break

if (mycount>comp_count):
	print "you won!"
	print mycount
elif (mycount<comp_count):
	print "computer wins"
	print comp_count
else:
	print "it is a draw"


#here i'm done
