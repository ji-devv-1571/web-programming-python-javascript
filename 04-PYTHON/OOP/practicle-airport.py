class Flight():
    def __init__(self, capacity):
        if(type(capacity) == "string"):
            print("Please provide an integer")
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():  # it means if self.open_seats() == 0
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flightCapa = int(input("please input the flight capacity: "))
flight = Flight(flightCapa)

# print("peoples to add:")
# peopleList = input()
people = ["Harry", "Gawk", "Github"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully. 👌👌👌")
    else:
        print(f"Failed to add {person}, seats not available.")
