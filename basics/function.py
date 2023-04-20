def greet_user():
    """Display a simple greeting."""
    print("Hello!")
 
greet_user()

def greet_user(username):
 """Display a simple greeting."""
 print("Hello, " + username.title() + "!")
 
greet_user('jesse')

#Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
 
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')


#Keyword Arguments
def describe_pet(animal_type, pet_name):
 """Display information about a pet."""
 print("\nI have a " + animal_type + ".")
 print("My " + animal_type + "'s name is " + pet_name.title() + ".")
 
describe_pet(animal_type='hamster', pet_name='harry')

# Default Values
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='willie')

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


# Return Values
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)


#Optional

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
 

# Arbitrary arguments Dictionary
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                              location='princeton',
                              field='physics')
print(user_profile)
