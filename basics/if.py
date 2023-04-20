# String
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
print("car == 'bmw': " + str(car == 'bmw'))
print("car == 'audi': " + str(car == 'audi'))
print("car == 'Bmw': " + str(car == 'Bmw'))
print("car.title() == 'Bmw': " + str(car.title() == 'Bmw'))

request_topping = 'mushrooms'

if request_topping != 'anchovies':
    print("Hold the anchovies!")


# Number

age = 18
print("age == 18: " + str(age == 18))

answer = 17

if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
print("age < 21: " + str(age < 21))
print("age <= 21: " + str(age <= 21))
print("age > 21: " + str(age > 21))
print("age >= 21: " + str(age >= 21))


# AND

age_0 = 22
age_1 = 18
print("age_0 >= 21 and age_1 >= 21: " + str(age_0 >= 21 and age_1 >= 21))

age_1 = 22
print("age_0 >= 21 and age_1 >= 21: " + str(age_0 >= 21 and age_1 >= 21))


# OR

age_0 = 22
age_1 = 18
print("age_0 >= 21 or age_1 >= 21: " + str(age_0 >= 21 or age_1 >= 21))

age_0 = 18
print("age_0 >= 21 or age_1 >= 21: " + str(age_0 >= 21 or age_1 >= 21))


# List

requested_toppings = ['mushrooms', 'onions', 'pineapple']
print("'mushrooms' in requested_toppings: " + str('mushrooms' in requested_toppings))
print("'pepperoni' in requested_toppings: " + str('pepperoni' in requested_toppings))

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you van post a response if you wish")


# Boolean

game_active = True
can_edit = False    

# if-else
age = 12
if age < 4:
 print("Your admission cost is $0.")
elif age < 18:
 print("Your admission cost is $5.")
else:
 print("Your admission cost is $10.")


available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
 
print("\nFinished making your pizza!")
