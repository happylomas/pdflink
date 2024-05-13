# Word guessing game

secret = 'good'
guess_count = 0
your_guess = ''
print('Welcome to a word guessing game')
print(' ')
output = ''
# your_guess = input('What is your guess? ')

while your_guess.lower() != secret.lower():
    your_guess = input('What is your guess? ')
    guess_count += 1
    if len(secret)!=len(your_guess):
        print('Your guess need to be four letters, Please try again.') 
    elif len(secret) == len(your_guess):
        for x in range(len(secret)):
            if secret[x].lower() == your_guess[x].lower():
                output += your_guess[x].upper()
            elif secret[x].lower() in your_guess.lower():
                output += your_guess[x].lower()
            else:
                output += '_ '
        if your_guess != secret:
            print('Your guess was not correct.')
            print(f'{output}')
            output=''
print('Congratulation! you guessed it.')
print(f' it took you {guess_count} guess to get it.')