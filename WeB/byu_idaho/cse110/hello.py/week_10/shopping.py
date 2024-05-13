item_list = []
price_list = []
item = None
print('Welcome to the shopping cart program')
print(' ')
print('Please select one of the following option by replying 1-5:')
print('')
options = ['Add Item', 'View Cart', 'Remove item', 'Compute Total', 'Quit']
for i in range(len(options)):
    option = options[i]
    print(f'{i +1}.{option}')
print('')
option1 = int(input('Please enter an action '))

while option1 == 1:
    item = input('what item will you like to add? ')
    print(f'{item} has been added to the cart')
