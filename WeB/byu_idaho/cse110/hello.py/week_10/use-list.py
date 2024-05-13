# shopping List


print('Please enter the items of the shopping list (type: quit to finish):')
shopping_list = []
item = None

print('')
while item != 'quite':
    item = input('item:')
    if item !='quite':
        shopping_list.append(item)

print('')
print('The shopping list is:')
# item = [ 'Milk', 'Bread', 'Candy', 'Carrots', 'quit']

for item in shopping_list:
    print(item)
print('')
# to print out items with numbers
print('The Shopping list with index')

print('')
for items in range(len(shopping_list)):
    item = shopping_list[items]
    print(f'{items}. {item}')

print()

index = int(input("Which item would you like to change? "))
new_item = input("What is the new item? ")

shopping_list[index] = new_item

print("\nThe shopping list with indexes is:")
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f"{i}. {item}")

