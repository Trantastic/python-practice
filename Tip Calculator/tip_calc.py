# Ask user their bill total
# Ask user how much they want to tip
# Take user input
# 	Bill total * tip % = result
# Print result to user

def calculate_tip():
	bill_total = int(input('How much is your bill? '))
	tip_per = int(input("How much would you like to tip? "))
	tip_amt = 0
	total = 0

	tip_amt = round((bill_total * (tip_per / 100)), 2) 
	total = bill_total + tip_amt

	print(f'Your tip amount is {tip_amt} and your total is {total}')

calculate_tip()