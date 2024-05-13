import math
# print(f'Welcome to the velocity calculator. Please enter the following:')

## Mass (in kg): 5
# #Gravity (in m/s^2, 9.8 for Earth, 24 for Jupiter): 9.8
## Time (in seconds): 10
## Density of the fluid (in kg/m^3, 1.3 for air, 1000 for water): 1.3
## Cross sectional area (in m^2): 0.01
## Drag constant (0.5 for sphere, 1.1 for cylinder): 0.5

## The inner value of c is: 0.003
## The velocity after 10.0 seconds is: 67.512 m/s

print(' ')
print(f'Welcome to the velocity calculator. Please enter the following:')
print(' ')
M = float(input('Mass in kg: '))
g_E = float(input('Gravity on earth: '))
g_J = float(input('Gravity for Jupiter: '))
t = float(input('Time in seconds(t): '))  
P = float(input('Density of the fluid(in m/s^3, 1.3 for air, 1000 for whater: '))
A = float(input('Cross sectional area (in m^2): '))
C = float(input('Drag constant (0.5 sphere, 1.1 for cylinder): '))

## fomular for inner value c = (1 / 2) * p * A * C

print (' ')
c= (1/2)*P*A*C
v_time_E = math.sqrt(M * g_E / c) * (1 - math.exp((-math.sqrt(M * g_E * c) / M) * t))
v_time_J = math.sqrt(M * g_J / c) * (1 - math.exp((-math.sqrt(M * g_J * c) / M) * t))
print(' ')
print (f'the inner value of c is :{ c}')
print(f'The velocity after {t} seconds is: {v_time_E:.3f}m/s')
print(f'The velocity after {t} seconds is: {v_time_J:.3f}m/s')