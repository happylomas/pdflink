youngest_age = 7000
oldest_age = -2
youngest_name = ''  
oldeest_name = ''

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
    ]

for list in people:
    parts = list.split(' ')

    names = parts[0]
    ages = int(parts[1]) 

    if ages <  youngest_age:
        youngest_age = ages
        youngest_name = names
    
    if ages > oldest_age:
        oldest_age = ages
        oldeest_name = names

print('')

        
print(f"The youngest person is: {youngest_name} with an age of {youngest_age}")

print(f"The oldest person is: {oldeest_name} with an age of {oldest_age}")

        


    
    

