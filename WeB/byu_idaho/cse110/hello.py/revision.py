# print('Welcome to my Python Revession. \nI will try to run it to week14 the last week')
# print()
# fav_colour = input('Please type your favorite colour: ')
# print('Your favourite color is:')
# print(fav_colour)

# print('this is for exceeding requirment')
# nickname = input('What is your nick name:')
# print('your nick name is :')
# print(nickname)

## Commenting 

# print("it is it's good")


# distance = 9 * 1205 * 18

# # Scientific notation with 3 digits of precision
# print(f"The distance is: {distance:.3e} meters.")
# # Output: The distance is: 1.952e+05 meters.

# # Scientific notation with 6 digits of precision
# print(f"The distance is: {distance:.6e} meters.")
# # Output: The distance is: 1.952100e+05 meters.

# from datetime import datetime, timedelta

# today = datetime.now()
# day = timedelta(days=1)
# yesterday = today - day
# print(f'{today}')
# print(f'yester day was {yesterday}')

# print()
# print('to day is: ' + str(today))
# print('yesterday was: ' + str(yesterday))


# # Start with the number 1
# number = 1

# # Keep looping as long as the number is less than or equal to 5
# while number <= 5:
#     # Display the number
#     print(f"The number is: {number}")
    
#     # Update the number to be one more than it was
#     number = number + 1 

# print("Finished with the loop")

# guess_count = 0
# total = 0
# scoretimes = 5
# while guess_count <= scoretimes:
#     print(guess_count)
#     score = int(input('enter a score: '))
#     total = total + score
#     print(total)
#     print()
#     print(guess_count)
#     guess_count += 1

# word = "book"
# number_of_letters = 4

# for index in range(number_of_letters):
#     # index += 1
#     letter = word[index]
#     print(f"Index: {index} Letter: {letter}")
#     print(index)

word = "book"
number_of_letters = len(word) # Notice this can now work for any string
print(number_of_letters)
print()

for index in range(number_of_letters):
    # print(index)
    letter = word[index]
    print(f"Index: {index} Letter: {letter}")