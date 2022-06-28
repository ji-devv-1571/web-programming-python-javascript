# the __init__ will be called automatically when the class will called.
# the self parameter will provided automatically
# self.x is a variable that stores the input1 parameter's value, you can call it whatever you want.

class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2


p = Point(2, 3)

print(f"p.x = {p.x}, p.y = {p.y}")
