
#Import random to get a random number for determining a random sequence for testing
#also import os so that we can see all the files in the current directory
#Maybe soon i will make it smart so that you can't really fuck up the options
import random
import os

# "." means this directory
files=os.listdir(".")
#print(files)

#The following function is a recursive function to generate a sequence of random numbers without repeating
#We do this so that we can call random kanji out of order to make it harder
def genorder(minval,maxval,order):
	#print("min and max are ",minval,maxval)
	if (maxval-minval)==1:
		order.append(maxval)
		order.append(minval)
		return 0
	if(minval>maxval):
		return 0
	if(maxval==0):
		order.append(0)
		return 0
	if(maxval-minval)==0:
		order.append(minval)
		return 0
		
	valprev=random.randint(minval,maxval)
	order.append(valprev)
	#print("picked ",valprev)
	
	genorder(minval,valprev-1, order)
	genorder(valprev+1,maxval, order)		

	return order
	
#END FUNCTION 	



#Here will be a function to open file and read its contents into an array for us to make things look neater below
def GetData(filen,useLen,numK):
	print("Ok im going to open file now.")
	print("enter 0 at any time to stop. Remember to write out Kanji so you get good at writing too!\n\n\n")

	data=[]
	with open(filen, 'r', encoding="utf-8") as f:
		if useLen==1:
			data = f.readlines()
		else :                                          #In case we dont want to do all kanji at once! I should also make function to go between range of kanji huh? 
			for i in range(0,int(numK)+1):
				data.append(f.readline())
			
		f.close()

	return data

#END FUNCTION TO OPEN FILE AND GET KANJI DATA


#Here will be a function to split and pretty up data
def PrettyData(data, i):

	line=[]
	line=data[i].split(",")
	line[0]=(line[0].encode("utf-8")).decode("utf-8") #Probably redundant by encoding and decoding but better to be sure
	line[1]=(line[1].encode("utf-8")).decode("utf-8")

	return line

#END FUNCTION FOR MANIPULATING FILE STRINGS



#Here will be a function to compare user entered data... god I wish pointers existed or that I used C....
def Match(usrval,correctval):
	#Split the correctval up by / in case it has multiple meanings and we dont want to make usr guess all in watver order
	vals=correctval.split("/")

	#We do this so that if the user gets any of the deffs correct they get it correct, cause it was annoying before
	if len(vals)>1:
		for meaning in vals:
			if usrval==meaning:
				return 1
	
	#If it only has one meaning then check it 
	if usrval==correctval:
		return 1

	#else they got it wrong, return 0
	return 0

#END FUNCTION FOR MATCHING USER INPUT TO FILE DATA

# Lets make a function to grade them huh
def Grade(cor,tot):
	perc = (cor/tot)*100
	print("You got : ",perc,"% correct")
	if perc>=60 and perc<70:
		print("\n\n   Final Grade:   D   Terrible   \n\n")
	elif perc>=70 and perc<80:
		print("\n\n   Final Grade:   C   Needs work!!  \n\n")
	elif perc>=80 and perc<90:
		print("\n\n   Final Grade:   B    OK!  \n\n")
	elif perc>=90:
		print("\n\n   Final Grade:   A    Excellent!!! \n\n")
	else:
		print("\n\n   Final Grade:   F    Fail  \n\n")
	
	return 0

#A function to search for the Kanji by typing in english word??? through all files?? 
def FindKanji(englishWord):

	return 0;    #Zero if we found it ig

#END said function
def starting_option():

	main_menu_options = {0: "Study Mode", 1: "Random Test Grade _", 2: "Test all Grades", 3: "Test up to Grade _"}

	print("what do you want to do?")
	for option in main_menu_options:
		print(("{}: {}").format(option, main_menu_options[option]))

	return(input())

def print_lines(data):
	for i in range(0,len(data)-1):

		line=PrettyData(data, i)
		print("\n",line[0],"   ",line[1],"    ",line[2],"\n")
		nl=input()
		if nl=="0":
			break

def study_mode():
	print("Enter the grade you want to study upon ")	#Get grade from user so we know what file to openen
	grade=input()
	uselen = 0
	print("how many of the Kanji do you want to study? Enter all for all of them")
	numkanji=input()

	if numkanji.lower()=="all":
		uselen=1
		#Open file, get data, close file, populate data list

	filen="./kanji"+grade+".txt" 
	data=GetData(filen,uselen,numkanji)

	print_lines(data)

def test_x():
	print("Enter the grade you want to study upon ")	#Get grade from user so we know what file to openen
	grade=input()
	filen="./kanji"+str(grade)+".txt"                        #Get our filename to open the correct grade 
	line=[]                                             #Line holds the contents seperated by , ' s
	i=0
	data=[]
	order=[]
	correct=0
	wrong=0
	total=0

	data=GetData(filen,1,0)                                  #Open file and get data
	order = genorder(0,len(data)-1, order)                              #Generate a random sequence to print kanji

	for i in order:

		line=PrettyData(data, i)
		
		print("    ",line[0],end="    ")
		inp=input()
		if inp=="0":
			break
		
		ans = Match(inp.lower(),(line[2].strip()).lower())
		
		if ans==1:                                            #If correct tell them correct and keep track of how many 
			correct=correct+1
			print("\n     correct!  \n\n")
			
		else:                                                 #If wrong tell hem what it was, keep track of how many wrong
			wrong=wrong+1
			print("\n oooof sorry bub, not correct, correct response was : ", end="  ")
			print("   ",line[2] )
			
		total=total+1                                         #incriment total so if we break we know how many we did
		
	print("you got : ",correct, " out of : ",total," attempted correct response ")
	Grade(correct,total)                                      #Give them a letter grade

def main():

	go_again = True

	run_options = {0: study_mode, 1: test_x}

	answr=starting_option()

	while go_again == True:
		run_options.get(int(answr))()
		print("want to go again? 1=yes ")
		loopanswr=input()
		if loopanswr == 1:
			go_again = True
		else:
			go_again = False

	print("good job!!!")

while True:
	main()