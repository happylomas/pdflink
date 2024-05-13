# ## Word Game

# start = input('Do you want to play a game? ')
# if start.capitalize() == 'YES':
#     A = Truth or Dare
#     B = Hide and Seek
#     choice = input('DO you like to play TRUTH_ ')
# else:
#     print('Are you sure you wan to Quite? ')
#     if 
#     print('Which word game do you wan to play? ')
# if 
#     # game = 'truth or dare'
#     # game = 'Hide and seek'
# else:
#     print('Are you sure you want to quit this game? ')

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


start = input(colors.GREEN + 'Do you wan to play a game? ' + colors.YELLOW)

if start.upper()== 'YES':
    choice = input(colors.GREEN + 'Do you wan to play HIDE or TRUTH? '+ colors.YELLOW)
    if choice.upper() == 'HIDE':
        print(' ')
    
        choice2 = input(colors.GREEN +'You are walking through a dark forest and find two items:'
                    'a MATCH and a FLASHLIGHT.\nWhich one do you want to pick up? '+ colors.YELLOW)
        if choice2.upper() == 'MATCH':
            print(' ')
            choice3 = input(colors.GREEN +'You pick up the match and strike it, the forest around you is illuminated.\n'
            'You see a large grizzly bear, and then the match burns out.\n Do you want to RUN, or HIDE behind a tree? '+ colors.YELLOW)
            if choice3.upper() == 'HIDE':
                print(' ')
                print(colors.GREEN +'You are save !!!'+ colors.ENDC)
            else:
                print(colors.GREEN +'You are Dead !!!'+ colors.ENDC)

        else:
            choice4 = input(colors.GREEN +'You pick up the flashlight and turn it on. You see the pathway lit up in front of you,\n'
                   'but you thought you also heard something off to the side. \n Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise? '+ colors.YELLOW)
            if choice4.upper() == 'LOOK':
                print(colors.GREEN +'Sorry You cannot find anything, Game Over!!')
            else:
                print(colors.GREEN +'Let us hope you will Follow the right path. You win the Game!!.'+ colors.ENDC)
    else:
        choice.upper() == 'TRUTH'
        choice2 = input(colors.GREEN +'TRUTH or DARE? '+ colors.YELLOW)
        if choice2.upper() == 'TRUTH':
            choice3 = input(colors.GREEN +'You choose truth, what is your favourite food?  '+ colors.YELLOW)
        else:print(colors.GREEN +'You choosed  DARE, I dare you to jump from the window.'+ colors.ENDC)
else:
    print('Goodbye!!!')       

print(' ')
print(colors.GREEN +'Thank you for Playing, Come back tomorrow and earn reward.'+ colors.ENDC)





