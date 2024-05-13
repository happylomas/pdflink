# # team activity 

class colors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

import random

keep_playing = 'yes'
while keep_playing== 'yes':
    magic_number = random.randint(1, 10)
    print('')
    guess = -1
    guess_count = 0
    
       
    while guess != magic_number:
    #    magic_number = int(input('what is the magic number? '))
        guess = int(input(colors.BLUE +'What is your guess? '+ colors.ENDC) )

        guess_count = guess_count + 1

        if guess < magic_number:
             print('higher') 
        elif guess > magic_number:
             print('Lower')
        else:
            print('You guessed it!')
    print(f'you guessed {guess_count} times')

    keep_playing = input('Do you want to play again (yes/no)?')
print('Thank you for playing')



    




