import math
from datetime import datetime
# open(filename, mode="rt")
# with open("volumes.txt", "r") as file:
#     data = file.read()
#     print(data)


print('Welcome to tire volume calculator')
print()
# current date time
current_date_and_time = datetime.now()
print(f"{current_date_and_time:%Y-%m-%d}")
print()
width = int(input('Enter the width of the tire in mm (ex 205): '))
ratio = int(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = int(input('Enter the diameter of the wheel in inches (ex 15): '))

# i will divide the math formular into 3 path so the math will be easy for me,
#  and i will name them alpa, beta and garma

alpha = math.pi * width**2 * ratio
beta = (width * ratio) + (2540 * diameter)
garma = (alpha * beta) 
volume = garma / 10000000000

# rounding to 2 decimal places 
volume = round(volume, 2)
print(volume)

if width >= 150 and width < 200:
    price = 100
elif width >= 200 and width < 250:
    price = 150
elif width >= 250 and width < 300:
    price = 200
else:
    price = 500


with open("volumes.txt", "a") as file:
    file.write(f"{current_date_and_time:%Y-%m-%d}, {width}, {ratio}, {diameter}, {volume}, {price} \n")

with open("volumes.txt", "r") as file:
    data = file.read()
    print(data)
   


