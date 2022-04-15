# CTI-110
# P2HLAB1 - Warm up: Variables, input, and type conversion
# Todd Henderson
# 15 April 2022
# Creating Variables, input, and type conversion
# Intilize Accumulator
user_int = int(input("Enter integer (32 - 126):\n"))
user_float = float(input("Enter float here: \n"))
user_charec = input("Enter character here: \n")
user_string = input("Enter string here: \n")

print(user_int,user_float,user_charec,user_string)
print(user_string,user_charec,user_float,user_int)
print(user_int,user_float,user_charec,user_string)
chr(user_int)
print(user_int,"Converted to a character is",chr(user_int))

"""FIXME (1): Finish reading other items into variables, then output the four values on a single line separated by a space
Enter integer (32 - 126):
99
Enter float:
3.77
Enter character:
z
Enter string:
Howdy
99 3.77 z Howdy"""
# FIXME (2): Output the four values in reverse

# FIXME (3): Convert the integer to a characer, and output that character