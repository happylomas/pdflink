# # guess with count of number of guess

# import random

# keep_playing = "yes"

# while keep_playing == "yes":
#     magic_number = random.randint(1, 10)
#     count = 0
#     guess = 6

#     while guess != magic_number:
#         guess = int(input("What is your guess? "))
#         count = count + 1

#         if guess < magic_number:
#             print("Higher")
#         elif guess > magic_number:
#             print("Lower")
#         else:
#             print("You guessed it!")


#     print(f"It took you {count} guesses")

#     keep_playing = input("Would you like to play again (yes/no)? ")

# print("Thank you for playing. Goodbye.")


# word = "book"
# number_of_letters = len(word) # Notice this can now work for any string

# for index in range(number_of_letters):
#     letter = word[index]
#     print(f"Index: {index} Letter: {letter}")



# store the secret word
secret_word = 'faith'

hide = ''

for letter in secret_word:
    hide = hide + '_ '

print(f'Your hint: {hide}')
guess_count = 0
guess = ''


while guess.lower() != 'faith':
    guess_count += 1
    letter= '_'
    hide = ''
    guess = input('What is your guess? ')
    if len(guess.lower()) == len(secret_word):
            for l, j in enumerate(guess.lower()):
                letter = '_'
                for b, f in enumerate(secret_word):
                    if (l == b and j == f):
                        letter = j.capitalize()
                    else:
                        if (j == f):
                            letter = j + ''
                hide = hide + letter 
            print(f'Your hint is :{hide}')
    else: 
        print('Sorry, Your guess word must be the same length as the word.',len(secret_word))
        if guess == secret_word:
            print('Congratulations! You guessed it!')           
    

      
print(f'It took you {guess_count} guesses.')