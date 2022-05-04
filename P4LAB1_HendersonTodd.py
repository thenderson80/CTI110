# CTI-110
# P4LAB1 - Count Input Length
# Todd Henderson
# 9 May 2022

user_text = input("Insert text here: ")
chars_to_remove = (" .,")
for character in chars_to_remove:
	user_text = user_text.replace(character, "")
	if character not in chars_to_remove:

			char_count =+ 1
# 	print the string 
print(len(user_text))