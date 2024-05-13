## Precticing If Statement.

# What is the first number? 4
# What is the second number? 3
# The first number is greater
# The numbers are not equal
# The second number is not greater

# What is your favorite animal? giraffe
# That one is not my favorite.

first_number = int(input('What is the first number? '))
second_number = int(input('What is the second number? '))
print(' ')
if first_number > second_number:
    print('The first number greater')
else:
    print('The first number is not greater')

print(' ')
if first_number==second_number:
    print('The numbers are equal')
else:
    print('The numbers is not  equal')
    print('')
fav_animal = input('What is your favorite animal? ')
if fav_animal.lower() == 'dog':
    print('That is my favourite animal too!')
else:
    print('That one is not my favourite.')