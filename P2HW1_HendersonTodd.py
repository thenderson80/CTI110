# Variables and Expressions Assighnment
# 5 April 2022
# CTI-110 P2HW1 - Total Purchases
# Todd Henderson
#
num1 = float (input("Enter the price of item #1: $"))
num2 = float (input("Enter the price of item #2: $"))
num3 = float (input("Enter the price of item #3: $"))
num4 = float (input("Enter the price of item #4: $"))
num5 = float (input("Enter the price of item #5: $"))
print("")
# The sum of five items
print("-------RESULTS-------")
pretax = num1 + num2 + num3 + num4 + num5
pretax = float("{0:2f}".format(pretax))
print("Subtotal: $",pretax)
"""Show and compute the state and county sales tax on those combined purchases and calculate the total of taxes"""
CountySalesTax = pretax * .07
CountySalesTax = float("{0:2f}".format(CountySalesTax))
print("Sales Tax: $",CountySalesTax)
posttax = pretax + CountySalesTax
posttax = float("{0:2f}".format(posttax))
print("Total: $",posttax)

