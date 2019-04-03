'''
Description:
	The user enters a cost and then the amount of money given. 
	The program will figure out the change and the number of quarters, 
	dimes, nickels, pennies needed for the change.
'''

def calculate_change(cost, amount_given):
	cost = int(cost*100)
	amount_given = int(amount_given*100)
	change = amount_given - cost
	print(change)

	change_type = { 'Quarter': 25, 'Dime': 10, 'Nickel': 5, 'Penny': 1 }
	change_count = { 'Quarter': 0, 'Dime': 0, 'Nickel': 0, 'Penny': 0 }


	for key, value in change_type.items():
		while change - value >= 0:
			change -= value
			change_count[key] += 1

	# 1.37 = 5 quaters 1 dime 2 pennies
	return change_count



def main():
	cost = float(input('Enter the cost: '))
	amount_given = float(input('Enter the amount amount provided: '))
	assert amount_given >= cost

	change = calculate_change(cost, amount_given)
	print(f'Your change is: \n {change}')

if __name__ == "__main__":
	main()