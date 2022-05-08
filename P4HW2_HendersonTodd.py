def ask_num_customers_and_num_eaters():
    num1 = int(input("How many students do you want to order pizza for? "))
    num2 = float(input("Enter number of people per pizza (1.5, 2 or 3): "))
    return num1, num2

def calculate_and_print_pizza_order():
    print("----Pizza Order--------")
    # Total Number of Pizzas
    print(f"Number of Students: ",num1)
    total_pizzas = num1 / num2
    total_pizzas = round(total_pizzas)
    net_cost = 5 * total_pizzas
    tax = net_cost * 0.06
    cost = net_cost + tax
    print(f"Pizzas Needed:      ", total_pizzas)
    print(f"Price                ${cost:.2f}")
    print("____________________________")

def inform_invalid_entry():
    print("INVALID ENTRY!!!")
    print("Should have entered 1.5, 2 or 3")

restart = True

while restart == True:
    
    num1, num2 = ask_num_customers_and_num_eaters()
    
    if num2 in [1.5, 2,3]:
        calculate_and_print_pizza_order()
        restart1 = input("Run program again? (y for yes) \n")
        if restart1.lower() == "y":
            pass
        else:
            restart = False
            print("Bye")
    
    else:
        inform_invalid_entry()
        continue