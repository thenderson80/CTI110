# # CTI-110
# P5HW2 - Score List
# 9 May 2022
# Todd Henderson

import random
# Constants for the menu choices
ADD_RANDOM_NUM_CHOICE = 1
SUBTRACT_RANDOM_NUM_CHOICE = 2
QUIT_CHOICE = 3

# The main function

def main():
# The choice variable controls the loop
# and hold the user's menu choice
	
	choice = 0
	
	while choice != QUIT_CHOICE:
						
# display menu
		display_menu()
		
# get user's choice
		choice = int(input("Please chose one of the menu options: "))
		
# Add two random numbers
		if choice == ADD_RANDOM_NUM_CHOICE:
			add1 = random.randint(1, 50)
			add2 = random.randint(1, 50)
			add3 = add1 + add2
			print(add1,"+", add2)
			print("")
			
			attempt_counter = 0
			done = False
			while not done:
				attempt_counter += 1
				add4 = int(input("Enter answer: "))
				if add4 == add3:
					print("Congratulations!!! You got the answer correct after", attempt_counter, "tries...")
					done = True
				else:
					if add4 > add3:
						print("Sorry, guess is too high.")
						print("")
					if add4 < add3:
						print("Sorry, guess is too low.")
						print("")

		elif choice == SUBTRACT_RANDOM_NUM_CHOICE:
				sub1 = random.randint(1, 50)
				sub2 = random.randint(1, 50)
				sub3 = sub1 - sub2
				print(sub1,"-",sub2)
				print("")
				
				attempt_counter = 0
				done = False
				while not done:
					attempt_counter += 1
					sub4 = int(input("Enter answer: "))
					if sub4 == sub3:
						print("Congratulations!!! You got the answer correct after", attempt_counter, "tries...")
						done = True
					else:
						if sub4 > sub3:
							print("Sorry, guess is too high.")
							print("")
						if sub4 < sub3:
							print("Sorry, guess is too low.")
							print("")
									
	else:
		print("Error: invalid entry")
			
	# display menu options
def display_menu():
	
	print("Welcome to Math Quiz")
	print("")
	print("MAIN MENU")
	print("------------------------------")
	print("1.  Adding Random Numbers")
	print("2.  Subtracting Random Numbers")
	print("3.  Exit")
	print("")

	
if __name__ =="__main__":
	main()