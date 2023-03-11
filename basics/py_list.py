bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0].title())
print(bicycles[3])
print(bicycles[-1])

# Changing
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding
motorcycles.append('honda')
print(motorcycles)
motorcycles.insert(0, 'harley')
print(motorcycles)

# Removing
del motorcycles[-1]
print(motorcycles)

popped_motorcycle = motorcycles.pop() 
print(motorcycles)
print("popped_motorcycle: " + popped_motorcycle)

last_owned = motorcycles.pop() 
print("The last motorcycle I owned was a " + last_owned.title() + ".")

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles.remove('yamaha') # Remove the first occurence
print(motorcycles)


# Sorting
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
bicycles.sort()
print(bicycles)
bicycles.sort(reverse=True)
print(bicycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars)) # Sorted method keeps the original list, different than Sort
print("\nHere is the original list again:")
print(cars)
cars.reverse()
print(cars)

# Length
print(len(cars))


# Loops
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician.title() + ", that was a great trick!") 
    print("I can't wait to see your next trick, " + magician.title() + ".\n")
 
print("Thank you, everyone. That was a great magic show!")

# Range
for value in range(1,5):
    print(value)

even_numbers = list(range(2,11,2)) 
print(even_numbers)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
min(digits)
# 0
max(digits)
# 9
sum(digits)
# 45    

# Slicing a List
players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
friend_foods.append("ice cream")
print("\nMy friend's favorite foods are:")
print(friend_foods)

# Tuples
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
 print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
 print(dimension)
