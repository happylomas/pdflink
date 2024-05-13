#week 1, display and use of input and conversion if strings to intigers
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
# get the age of the users, 
text = input('Please enter your age: ')

# convert the age to an integer 
age = int(text)

# compute the slowest fastest hear rate
max_rate = 220 - age
slowest = max_rate * 0.65
fastest = max_rate * 0.85

# print out both spring and intgers with an f function
print(f'When you exercise to strengthen your heart, you should')
print(f'keep your heart rate between {slowest:.0f} and {fastest:.0f}')
print(f'beats per minute')