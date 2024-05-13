# have user type list of numbers and aprend to a list.abs(x

print("Enter a list of numbers, type 0 when finished.")
print('')
numbers = []
number = -1

while number != 0:
    number = int(input('Enter a number:'))
    if number != 0:
        numbers.append(number)
for number in numbers:
    print(number)
# sum
sum = 0
for number in numbers:
    sum += number
print(f'The sum is: {sum}')

# average = sum / range
cont = len(numbers)
average = sum / cont
print(f'The average is :{average}')

