# CTI-110
# P2HLAB2 - Input and formatted output: House real estate summary
# Todd Henderson
# 15 April 2022
# Input and formatted output
# Current prince and last months price
current_price = int(input("What is the current price of the house?: $"))
last_months_price = int(input("What was the price last month?: $"))
# Current Price information
diff = current_price - last_months_price
print(f"This house is ${current_price}.",end=" ")
print(f"The change is ${diff} since last month.")

your_value = (current_price * 0.051) / 12
print("The estimated monthly mortgage is $",end="")
print(f"{your_value:.2f}",end="")
print(" per month.")



"""print("The estimated monthly mortgage is $", f"{your_value:.2f}", sep='') or print(1, 2, sep='banana')"""