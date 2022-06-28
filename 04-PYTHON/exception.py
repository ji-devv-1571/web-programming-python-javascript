import sys

# exception means error

# x = int(input("x: "))
# y = int(input("y: "))
# # if you set y = 0, ZeroDivisionError will be raised
# result = x / y

# print(f"{x} / {y}  = {result}")

# rather than returning Traceback massy error, lets return a nice looking message

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: the input value is not an integer")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print(f"Error: Cannot divide {x} by {y}")
    sys.exit(1)

print(f"{x} / {y}  = {result}")
