alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned "+str(new_points)+" points!")

# Empty
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
alien_0['x_position'] = 0
alien_0["y_position"] = 25
print(alien_0)

# Chaging
alien_0 = {'color': 'green'}
print("The alien is "+alien_0['color']+".")

alien_0['color'] = 'yellow'
print("The alien is "+alien_0['color']+".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':  
   x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))


## DEL
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


favorite_languages = {
    'jen': 'python',
     'sarah': 'c',
     'edward': 'ruby',
     'phil': 'python',
     }
print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() +
    ".")

# loop
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)


favorite_languages = {
    'jen': 'python',
     'sarah': 'c',
     'edward': 'ruby',
     'phil': 'python',
     }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is "+
          language.title() + ".")  

# all keys
for name in favorite_languages.keys():
    print(name.title())

# Sorted
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# all values
for languages in favorite_languages.values():
    print(name.title())

# Nesting
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if (alien['color']=='green'):
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print("...")

print("Total number of aliens: "+str(len(aliens)))


# List in a Dictionary
favorite_languages = {
 'jen': ['python', 'ruby'],
 'sarah': ['c'],
 'edward': ['ruby', 'go'],
 'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


# Dictionary in a Dictionary        
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
         'last': 'curie',
         'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
    