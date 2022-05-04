# CTI-110
# P5LAB1_HendersonTodd
# Todd Henderson
# 10 May 2022

def laps_to_miles(user_laps):
	user_miles = user_laps*0.25
	return user_miles

if __name__ == "__main__":
	user_laps = float(input("How many laps did you complete? "))
	print(f"You walked {laps_to_miles(user_laps):.2f} miles")