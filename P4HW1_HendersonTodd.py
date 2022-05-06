# CTI-110
# P4HW2 - Score List
# Todd Henderson
# 9 May 2022
def scores():
	score = []
	assign = int(input("How many grades are you going to enter? "))
	# Intilize Accumulator
	TotalScore = 0
	scores = []
	
	for i in range(1, assign+1):
		num = float (input (f"Enter percentage ↓{i}: "))
		while num >100 or num <0:
			print("INVALID Score entered!!")
			print("Score should be between 0 and 100 ")
			num = float (input ("Please enter score again"))
		scores.append(num)
	print("-------------RESULTS-------------")
	# Find/print the lowest score
	print("Lowest score   : ",min(scores))
	scores.remove(min(scores))
	print("Modifies List  : ",scores)
	len(scores)
	avg = sum(scores) / len(scores)
	print("Scores Average : ",avg)
	print_grades(avg)
	print("---------------------------------")
	# Letter grades for def
def print_grades(avg):
	if 0 < avg < 60:
		print(f"Grade {avg} is a F")
	elif 60 < avg < 69:
		print(f"Grade {avg} is a D")
	elif 70 < avg < 79:
		print(f"Grade {avg} is a C")
	elif 80 < avg < 89:
		print(f"Grade {avg} is an B")
	elif 90 < avg < 99:
		print(f"Grade {avg} is a A")
		
		
		
scores()