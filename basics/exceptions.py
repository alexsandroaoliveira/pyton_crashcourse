try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")

# else block
try:
    answer = 5/1
except ZeroDivisionError:
    print("You can't divide by 0!")
else:
    print(answer)

    # Silently
try:
    print(5/0)
except ZeroDivisionError:
    pass