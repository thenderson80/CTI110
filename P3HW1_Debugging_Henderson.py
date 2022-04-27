# CTI-110
# P3HL1 - Debugging
# Todd Henderson
# 29 April 2022
# Creating a program within another program. Using the main () function.
# Debugging/Main()

def main ():
    print("Hello World!")# This program takes a number grade and outputs a letter grade.

# system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50
    
# TO DO: define the rest of the scores

    score = float(input("Enter grade: "))

if score >= 90:
    print("Your grade is: A")
elif score>=80 and score<=89: 
     print("Your grade is: B")
elif score>=70 and score<=79:
    print("Your grade is: C")
elif score>=60 and score<=69:
    print ("Your grade is: D")
else:
    print('Your grade is: F') # TO DO: finish this
    
# program start
main()