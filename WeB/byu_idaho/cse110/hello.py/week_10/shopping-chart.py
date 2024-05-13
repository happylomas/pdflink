# Display the contents of the shopping cart
# Remove an item (only needed for the final project deliverable)
# Compute the total (only needed for the final project deliverable)

item_list = []
price_list = []
item = None
print(' ')
print('Please select one of the following option by replying 1-5:')
print('')
options = ['1. Add Item', '2. View Cart', '3. Remove item', '4. Compute Total', '5. Quit']
# for i in range(len(options)):
#     option = options[i]
#     print(f'{i +1}.{option}')
option = 0
# for i in options:
#     print(i)
while option != 5:
    print(f'\nPlease select one of the following')
    for i in options:
        print(i)
    option = int(input(f'\nWhat will you like to do? '))
    print('')
    if option == 1:
        print('Please add the list of your shopping items here.')
        item = input('what item would like to add? ')
        price = float(input(f'\nwhat price is {item}? $'))
        print(f'{item} has been added to the shppoing cart')
        item_list.append(item)
        price_list.append(price)
            # print(f'\nPlease select one of the following')

            # for i in options:
            #     print(i)
    elif option == 2:
        for i in range(len(item_list)):
            print(f'{i+1}. {item_list[i]} - {price_list[i]}')
            # for i in options:
            #     print(i)
                
            print('')
    elif option == 3:
        remove = int(input('What item will you like to remove? '))
        remove -= 1
        item_list.pop(remove)
        price_list.pop(remove)
            # for i in options:
            #     print(i)

    elif option == 4:
        total = 0
        for j in range(len(price_list)):
            total += price_list[j]
        print(f'The total price in the shopping cart is ${total} ')
    elif option == 5:
        print('We gift you a candy for shopping with us!')
        print('Goodbye!')
        


