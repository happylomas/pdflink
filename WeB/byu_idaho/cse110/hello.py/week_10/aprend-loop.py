# The use of Aprend. in loop

friends_list = []
names = None
print('')

while names != 'end':
    names = input('Type the name if a friend:')
    if names != 'end':
        friends_list.append(names)
print('')
print('Your friends names are: ')
for friends in friends_list:
    print(friends)
