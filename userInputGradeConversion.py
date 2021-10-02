#


# Authors:			Theo Allen & Joe Foley
# Assignement 2:	User Input
#Course				Intro to Computer Programing
#Prof: 				Alam Miah
#Date: 				Oct 2, 2021
# Goal:				To develop an automatic Grade converter from numeric
#                   to letter ,e.g., 
#					User enters 89 abnd the machine returns
# 					"Your Grade is a B+"


print("Hello Theo")
'''

Hello Theo:
Is this what the prof is after?
I am often not on the smae wave length as the prof.
I think I am asnsering the HW question but I use 
the wrong technique or some such mistake.  Can you carefully read the Q
and decide if this is what he is after?

PLEASE pay close attention to the instructions
becasue I dont!

Here is what I did.
In Part A
I did a series of IF | ELIF statements.

In Part B
I copied what the teacher gave us but  changed
# your name to your grade

In Part C 
I tried to join the two together

In the past I have not read his HW questions 
# carefully enough so we need you to check me out on that.

We also need to add more explanatory comments.
Do you know about git hub?
'''

'''
# PART A
# Your Score converter

yourScore = 45  # <------------------ Change the score
if yourScore >= 95:
	print("A")
elif yourScore >= 90:
	print("A-")
elif yourScore >= 86:
	print("B+")
elif yourScore >=84:
	print("B")
elif yourScore >= 80:
	print("B-")
elif yourScore >= 76:
	print("C+")
elif yourScore >= 74:
	print("C")
elif yourScore >= 70:
	print("C-")
elif yourScore < 70:
	print("F")
'''

'''
# PART B
# USER NAME INPUT
numericGrade = input("Enter Numeric Grade: ")
print("Your Grade is : " + numericGrade)
'''

'''
#PART C
# Marry Parts A & B
yourScore = input("Enter Numeric Grade: ")
if yourScore >= 95:
	print("A")
elif yourScore >= 90:
	print("A-")
elif yourScore >= 86:
	print("B+")
elif yourScore >=84:
	print("B")
elif yourScore >= 80:
	print("B-")
elif yourScore >= 76:
	print("C+")
elif yourScore >= 74:
	print("C")
elif yourScore >= 70:
	print("C-")
elif yourScore < 70:
	print("F")
'''

#print("Your Grade is : " + numericGrade)


 

numericGrade = input("Enter Numeric Grade: ")
numericGrade = int(numericGrade)


if numericGrade >=95 and numericGrade <= 100 :  	# do have the "breaks at 
    print("Your Grade is A") 	 # the correct values???"
elif numericGrade >= 90 and numericGrade < 95:
    print("Your Grade is A-")
elif numericGrade >= 86 and numericGrade < 90:
    print("Your Grade is B+")
elif numericGrade >= 84 and numericGrade <86:
    print("Your Grade is B ")
elif numericGrade >= 80 and numericGrade < 84:
    print("Your Grade is B-")
elif numericGrade >= 76 and numericGrade < 80:
    print("Your Grade is C+")
elif numericGrade >= 74 and numericGrade < 76:
    print("Your Grade is C")
elif numericGrade >= 70 and numericGrade < 74:
    print("Your Grade is C-")
elif numericGrade >=0 and numericGrade < 70:
    print("Your Grade is F")
else:
	print("Only submit a value btwn 0 and 100")
# It might be nice to add a line that detects 
# if the user enterd something that was NOT
# a number, e.g., a letter or a punction mark, 
# or a special character.
