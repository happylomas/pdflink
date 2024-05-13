# import math
# # Calculating the speed of a falling object, using the formula:
# ​
# # v(t) = sqrt(mg/c) * (1 - exp((-sqrt(mgc)/m)t))
# ​
# print('Welcome to the velocity calculator. Please enter the following: ')
# ​
# m = float(input('Mass in kg: '))
# g_E = float(input('Gravity for Earth in (m/s^2): '))
# g_J = float(input('Gravity for Jupiter in m/s^2: '))
# t = float(input('Time in seconds: '))
# p = float(input('Density (in kg/m^3:) '))
# A = float(input('Cross sectional area (in m^2): '))
# C = float(input('Drag constant: '))
# ​
# #c = 1/2 p A C (formula for internal c)
# c = (1/2) * p * A * C
# v_time_E = math.sqrt(m * g_E / c) * (1 - math.exp((-math.sqrt(m * g_E * c) / m) * t))
# v_time_J = math.sqrt(m * g_J / c) * (1 - math.exp((-math.sqrt(m * g_J * c) / m) * t))
# ​
# ​
# #blank line
# print(' ')
# print(f'The inner value of c is: {c:.3f}')
# print(f'The velocity on Earth after {t}seconds is: {v_time_E:.3f}m/s')
# print(f'The velocity on Jupiter after {t}seconds is: {v_time_J:.3f}m/s')
# ​
# #print(' ')
# #STRETCH 1
# #bowling ball with radius 9
# #r_ball = float(input('Radius of the bowling ball: '))
# #A_ball = math.pi * (r_ball ** 2)
# ​
# #c_ball = (1/2) * p * A_ball * C 
# #V_time_ball = math.sqrt(m * g / c_ball) * (1 - math.exp((-math.sqrt(m * g * c_ball) / m) * t))
# ​
# #blank line
# #print()
# #print(f'The inner value of c for the bowling ball is: {c_ball}')
# #print(f'The velocity after {t:.3f}seconds is: {V_time_ball:.3f}m/s')
# ​
# #STRETCH 3
# # v_terminal = sqrt(mg/c)
# ​