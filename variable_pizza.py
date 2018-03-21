#####
#
# variable_pizza.py
#
# Created by: Sebastian N
# Created on: March 2
#
# This program calculates de cost of a pizza dependig on sizes and toppings
#
#####

# function for cost of pizza
def cost_pizza(toppings_passed_in, size_passed_in): 
	# If statement
	if (toppings_passed_in in my_toppings) and size_passed_in == 'Large':
		subtotal = (6.0 + (0.25+(toppings_passed_in*0.75)))
		tax = round((subtotal * 0.13)*100)/100
		total = (subtotal + tax)
		# Printing
		print 'Subtotal is: $', subtotal; print 'The taxt is: $', tax; print 'The total is: $', total

	elif (toppings_passed_in in my_toppings) and size_passed_in == 'Extra Large':
		subtotal = (10.0 + (0.25+(toppings_passed_in*0.75)))
		tax = round((subtotal * 0.13)*100)/100
		total = (subtotal + tax)
		# Printing
		print 'Subtotal is: $', subtotal; print 'The taxt is: $', tax; print 'The total is: $', total
	
	elif toppings_passed_in not in my_toppings:
		print 'Please input a valid amount of toppings (1 to 4)'

	elif size_passed_in != 'Large' or size_passed_in != 'Extra Large':
		print 'PLease input a valid size (Large or Extra Large)'

	else:
		print 'You should go to another store!'

# Variables
my_toppings = [1, 2, 3, 4]
size = raw_input('What size of pizza would you like? (Large or Extra Large): ')
toppings = input('How many toppings would you like? (Between 1 and 4): ')
toppings_number = int(toppings)


# Calling function
cost_total = cost_pizza(toppings_number, size)



