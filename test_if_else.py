day_name = "Thursday"
day = 27
temp = 80

print(f"Today is {day} {day_name} and it's  {temp} degrees outside")

lights_is_on = True

if lights_is_on:
    print("The light is on!")

car_is_red = False
if car_is_red:
    print("The color of this car is red!")
else:
    print("The color of the car is black")


weight = 128.4

if weight <= 195:
    print("You're under weight :)!")
else:
    print("You're over weight :(!")

age = 35

if age >= 18:
    print("They are an adult")
else:
    print("They are child")


import random

print(random.randint(1, 10))

print(random.random())

answer = random.randint(1, 3)
if answer == 1:
    print('yes')
elif answer == 2:
    print('maybe')
else:
    print('no')







