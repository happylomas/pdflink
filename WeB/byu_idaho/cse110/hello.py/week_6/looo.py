# trying loop

number = int(input('Please type a positive number: '))
while number <= 0:
    print(f'sorry that is a negative number. Please try again.')
    number = int(input('Please type a positive number: '))
else:
    print(f'The number is: {number}')


# May I have a piece of candy? no
print('')
print('')

reply = ''

while reply.lower() == 'yes':
    reply = input('May I have a piece of candy?  ')
print(f'Thank You')