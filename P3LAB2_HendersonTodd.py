# CTI-110
# P3LAB2 - 10.20.1 - Automotive Service Cost
# Todd Henderson
# 29 April 2022

prices = {
	'Oil change': 35,
	'Tire rotation': 19,
	'Car wash': 7,
}

service = input('Enter desired auto service: ')
print(f"You entered: {service}")
try:
	print(f"Cost of {service}: ${prices[service]}")
except KeyError:
	print(f"Error: requested service is not recognized")