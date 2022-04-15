# CTI-110
# P2HW2 - Score Avg
# Todd Henderson
# 5 April 2022
# Creating list for program
# Intilize Accumulator
scores =[]
input_string = input("Enter the students percentages in the next lines, press enter to continue.")
print("\n")
# Numbers to be averaged
for i in range(1, 8):
	Num = float(input(f"Enter score ↓{i}: "))
	scores.append(Num)
# Next displays the results of all the numbers
print("--------------Results--------------""\n")
print("Lowest score: ",min(scores))
scores.remove(min(scores))
print("Modifies List :",scores)
len(scores)
avg = sum(scores) / len(scores)
print("Scores Average", avg)