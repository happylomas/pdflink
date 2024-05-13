

print('Welcome to Wind Chill Calculator')
print('')
print('You can enter your temperature in celcuis or fahrenheit and indicate by replying c or f respectivily')

def windchil ():
    for v in range (0, 60, 5):
        v += 5

        if temperature == 'f':
            wind_fomular = 35.74 + (0.6215*temp) - (35.75*(v**0.16)) + (0.4275*temp*(v**0.16))
            print(f'At Temperature {temp}F, Wind speed at {v}mph. The windchill is: {wind_fomular:.2f}F')
        elif temperature == 'c':
            cel = (temp *9/5) + 32
            wind_fomular = 35.74 + (0.6215*cel) - 35.75*(v**0.16) + (0.4275*cel*(v**0.16))
            print(f'At Temperature {cel}F, Wind speed at {v}mph. The windchill is: {wind_fomular:.2f}F ')
        
        else:
            print('Try Again')

temperature = input('is the tempurature in fahrenheit or celsius unit (f/c)').lower()
temp = float(input ('What is the tempurature now? '))
print('')
windchil()