message = input("Tell me something, and I will repeat it back to you: ")
print(message)

age = input("How old are you? ")
age = int(age)
print(str(age >= 18))

# even_or_odd
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
 print("\nThe number " + str(number) + " is even.")
else:
 print("\nThe number " + str(number) + " is odd.")
 