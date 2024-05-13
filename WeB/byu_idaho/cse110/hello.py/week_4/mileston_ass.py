# milestone
child_meal = float(input('What is the Price of child meal? '))
adult_meal = float(input('What is the Price of Adult meal? '))
children_present = int(input('How many children are there? '))
adult_present = int(input('How many adults are there? '))
tax_rate = input('what is the sales tax rate? ')

drink = input('What drink do you prefer? ')
number_of_drink = float(input('How many drink do you want? '))
subtotal = float((child_meal * children_present) + (adult_meal * adult_present) + (number_of_drink*2))
print(' ')
print(f'Subtotal: ${subtotal:.2f}')
# print (f'Subtotal:{child_meal*children_present + adult_meal*adult_present}')
sales_tax = subtotal*6/100
print(f'Sales Tax: ${sales_tax}')
total = sales_tax+subtotal
print(f'Total:${total:.2f}')
# print(f'Sales Tax:{subtotal*6/100}')
print(' ')
payment = float(input('What is the payment amount? '))
change = payment - total
print(f'Change:${change:.2f}')
print(f'Thank you for patronizing us, we will be happy to serve you tomorrow')
print('')
print('')
print(f'I was able to meet basic requirments, including adding a drink and number of drinks collected.')
print(f'Thank you')

