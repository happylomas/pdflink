# # #favourite_colour = input('what is your favourite colour?\n')
# # #print(favourite_colour)

# # #best_teacher = input('who is your favourite teacher?')
# # #print(best_teacher)
# # #first = input('what is your first name?\n')
# # ##last = input('what is your last name?\n')
# # #print(first)
# # #print(last)
# # #print(first, last, "Age 26")
# # #ocupation = input('Data base manager')

# # #print('WORLD GAME')

# # #first = input('what is your first name?\n')
# # #last = input('what is your last name?\n')
# # #class_= input('What is your Class?\n')

# # #print('Please Enter The Following')
# # #adjective = input('Enter an adjective\n')
# # #animal = input('Enter an animal\n')
# # #verb = input('Enter a verb\n')
# # #exclamation = input('Enter an exclamation mark\n')
# # #verb = input('enter a verb\n')
# # #verb = input('enter a verb\n')
# # #print(f'The other day, I was really in trouble. It all started when I saw a very {adjective} , {animal} , {verb} , ')
# # #print(f'down the hallway. {exclamation}!')
# # #print(f'I yelled. But all I could think to do was to {verb}, over and over.')
# # #print(f'Miraculously, that caused it to stop, but not before it tried to {verb} right in front of my family.\n')
# # #print('Above is a word game presented by')
# # #print(first,last,  class_)


# # #age = 26
# # #print(f'How old are you + 'age')


# # #age = input('how old are?')
# # #print(f'on your next birthday, you will be 'age' +1')


# # #conversion of temperature
# # temperature = float(input('What is the Temperature in Fahrenheit? '))
# # temperature_c = (temperature-32)*5/9
# print(f'The temperature in celsius is {temperature_c:.1f} dgrees.')

# # Calculate meal' s subtotal for both adults and children subtotal = (child_price * number_children) + (adult_price * number_adults) 
# # Calculate sales tax sales_tax = float((subtotal * tax_rate) / 100) 
# # Calculate total bill total = subtotal + sales_tax


# print("For each of these questions, please provide a 1-10 rating:")

# loan_size = int(input("How large is the loan? "))
# credit = int(input("How good is your credit history? "))
# income = int(input("How high is your income? "))
# down_payment = int(input("How large is your down payment? "))



# should_loan = False

# if loan_size >= 5:
#     if credit >= 7 and income >= 7:
#         should_loan = True
#     elif credit >= 7 or income >= 7:
#         if down_payment >= 5:
#             should_loan = True
#         else:
#             should_loan = False
#     else:
#         should_loan = False
# else: # This means its a small loan
#     if credit < 4:
#         should_loan = False
#     else:
#         if income >= 7 or down_payment >= 7:
#             should_loan = True
#         elif income >= 4 and down_payment >= 4:
#             should_loan = True
#         else:
#             should_loan = False

# if should_loan:
#     print("The decision is yes. This is a good loan.")
# else:
#     print("The decision is no. You should not loan this money.")

# for i in range(5):
#     print(i)
#     for j in range(10, 13):
#         print(f"--{j}")
#         for k in range(1, 3):
#             print(f'--{k}')
# char  : 'a'
#string : 'abc'

# list[] mylist = [a, b, c, d]

#index     0     1    2
# mylist = ['abs', 'b', 'c']
# b = mylist[1]
# #       0123
# word = "book"
# number_of_letters = 4

# for i in range(0, number_of_letters):
#     letter = word[i]
#     print(f"Index: {i} Letter: {letter}")

# for letter in word:
#     print(letter)


# for loop understanding 

# colors = ["red", "blue", "green", "yellow"]
# for colour in colors:
#     print(colour)

# us a loop to show numbers from 1- 8

# number= 8
# for number in range(1, 9):
#     print(number)

# number= 8
# for number in range(2, 20, 2):
#     print(number)

print(' ')

# week  7 team practice

# word = 'commitment'

# favoruite_letter = input('what is your favourite letter? ')
# for letter in word:
#     if letter.lower() == favoruite_letter.lower():
#         print(letter.upper(), end='')
#     else:
#         print(letter.lower(), end='')

# print(' ')
# for letter in word:
#     if letter.lower() == favoruite_letter.lower():
#         print("_", end="")
#     else:
#         print(letter.lower(), end="")

# print()




# # game_list = []
# for x in range(len(secret)):
#     if secret[x].lower() == your_guess[x].lower():
#     # game_list.append(x) 
#         print(your_guess[x].upper())
#     elif secret[x] in your_guess[x]:
#         print(your_guess[x].lower())
#     else:
#         secret != your_guess
#         print('_')


# secret = 'good'
# guess_count = 0
# your_guess = ''
# print('Welcome to a word guessing game')
# print(' ')
# output = ''
# your_guess = input('What is your guess? ')

# while your_guess.lower() != secret.lower():
#     your_guess = input('What is your guess? ')
#     guess_count += 1
#     if len(secret)!=len(your_guess):
#         print('Your guess need to be four letters, Please try again.') 
#     elif len(secret) == len(your_guess):
#         for x in range(len(secret)):
#             if secret[x].lower() == your_guess[x].lower():


# for i in range(len(books)):
#     book = books[i]
#     print(f"{i}. {book}")


# x = 5

# x + 2

# print(x)

# print('')
# x = 5

# x += 1

# print(x)

# print('')

# largest = 0

# for value in my_list:

#     if value < largest:

#         largest = value

# print(f"The largest is {largest}")
# book = 'books'
# for i in range(len('books')):
#     book = 'books'[i]
#     print(book) 

# def display_regular(message):
#     print(message)

# def display_uppercase(message):
#     # This could be done on one line, without creating a new variable new_message
#     new_message = message.upper()
#     print(new_message)

# def display_lowercase(message):
#     new_message = message.lower()
#     print(new_message)

# The regular flow of the program starts here...
# user_message = input("What is your message? ")

# Pass this variable to each of the functions above to do their work
# display_regular(user_message)
# display_uppercase(user_message)
# display_lowercase(user_message)


# def display_numbers(x, y):
#     return 10

# x = 3
# y = 4
# x = display_numbers(x, y)

# print(x)


# Wind chill Alma
# def mat101():
sum = 0
for v in range(0, 60, 5):
    # print(v)
    v +=5
    print(v)
    # sum += v
    # total = sum / v
    # print(total)
    # # print(v)



