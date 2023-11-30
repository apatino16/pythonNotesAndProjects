# Problem 1 and 3

class Rectangle:
    # Problem 1: Initializes a new instance of Rectangle with default values
    def __init__(self, width, heigth, name="unnamed", x=0, y=0):
        # Initialize the attributes of the Rectangle object
        self.width = width  # Assigns the width of the rectangle
        self.height = heigth  # Assigns the height of the rectangle
        # Assigns a name to the rectangle (defaults to "unnamed")
        self.name = name
        self.x = x  # Assigns the x-coordinate (defaults to 0)
        self.y = y  # Assigns the y-coordinate (defaults to 0)

    # Calculates and returns the area of the rectangle
    def area(self):
        return self.width * self.height

    # Problem 3: Overriding the + operator to add two rectangles together
    def __add__(self, other):
        new_width = self.width + other.width
        new_heigth = self.height + other.height
        new_name = f"{self.name}_and_{other.name}"
        return Rectangle(new_width, new_heigth, new_name)

    # Override the comparison operators (<, >, <=, >=, ==, !=)
    # Problem 3: Overriding the < operator to compare rectangles' areas
    def __lt__(self, other):
        return self.area() < other.area()

    # Problem 3: Override the <= operator to compare rectangles' areas
    def __le__(self, other):
        return self.area() <= other.area()

    # Problem 3: Override the > operator to compare rectangles' areas
    def __gt__(self, other):
        return self.area() > other.area()

    # Problem 3: Override the >= operator to compare rectangles' areas
    def __ge__(self, other):
        return self.area() >= other.area()

    # Problem 3: Override the == operator to compare rectangles' areas
    def __eq__(self, other):
        return self.area() == other.area()

    # Problem 3: Override the != operator to compare rectangles' areas
    def __ne__(self, other):
        return self.area() != other.area()

    # Problem 1: Generates and returns a description of the rectangle
    def description(self):
        # Return a formatted string containing details of the rectangle
        return f"Name: {self.name}, Coordinates (x, y): ({self.x}, {self.y}), Width: {self.width}, Height: {self.height}, Area: {self.area()}"

    # Problem 3: # Override the str() function to print rectangle details
    def __str__(self):
        return f"Name: {self.name}, Coordinates (x, y): ({self.x}, {self.y}), Width: {self.width}, Height: {self.height}, Area: {self.area()}"

    # Problem 1: Updates the coordinates of the rectangle to new values
    def change_coords(self, new_x, new_y):
        self.x = new_x  # Updates the x-coordinate
        self.y = new_y  # Updates the y-coordinate
        # Print confirmation of updated coordinates
        print(f"Coordinates updated to ({self.x}, {self.y})")

# Testing the updated Rectangle class


# Create two rectangles
rect1 = Rectangle(10, 5, "Rectangle1", 2, 3)
rect2 = Rectangle(20, 7, "Rectangle2", 5, 5)

# Test addition of two rectangles
rect3 = rect1 + rect2
print("Result of adding rectangles 1 and 2:")
print(rect3)

# Test comparison of rectangles based on areas
print("Comparison of rectangles based on areas:")
# Check if area of rect1 is less than area of rect2
print(f"Rectangle 1 area < Rectangle 2 area: {rect1 < rect2}")
# Check if area of rect1 is equal to area of rect2
print(f"Rectangle 1 area == Rectangle 2 area: {rect1 == rect2}")
# Check if area of rect1 is not equal to area of rect2
print(f"Rectangle 1 area != Rectangle 2 area: {rect1 != rect2}")
# Check if area of rect1 greater than to area of rect2
print(f"Rectangle 1 area > Rectangle 2 area: {rect1 > rect2}")
# Check if area of rect1 is less than or equal to area of rect2
print(f"Rectangle 1 area <= Rectangle 2 area: {rect1 <= rect2}")
# Check if area of rect1 is greater than or equal to area of rect2
print(f"Rectangle 1 area >= Rectangle 2 area: {rect1 >= rect2}")


# Problem 2
class Vehicle:

    # Problem 2: Initializes a new instance of Vehicle with default values
    def __init__(self, nameV, speed):
        self.nameV = nameV  # Initialize the name of the vehicle
        self.odometer = 0  # Initialize the odometer to 0 (total miles driven)
        self.speed = speed  # Initialize the speed of the vehicle

    # Problem 2: Simulates the vehicle driving for a given amount of time
    def drive(self, minutes):
        # Problem 2: Calculate the distance traveled in the given time (minutes)
        # Speed is in miles per hour, calculate distance based on time
        distance = (self.speed / 60) * minutes
        self.odometer += distance  # Update the odometer with the traveled distance
        return distance  # Return the distance traveled in this trip


# Vehicle Class Test
# Instantiate Vehicle objects and test the class
# Creating a car object with a speed of 60 miles per hour
car1 = Vehicle("Car", 60)
# Creating a van object with a speed of 45 miles per hour
car2 = Vehicle("Van", 45)

# Problem 2: Test driving the vehicles
distance_traveled_car1 = car1.drive(30)  # Drive the car for 30 minutes
distance_traveled_car2 = car2.drive(45)  # Drive the van for 45 minutes

# Problem 2: Display the distance traveled and the updated odometer for each vehicle
print(f"{car1.nameV} traveled {distance_traveled_car1} miles. Odometer: {car1.odometer} miles.")
print(f"{car2.nameV} traveled {distance_traveled_car2} miles. Odometer: {car2.odometer} miles.")

# Problem 4


class Bicycle(Vehicle):

    def __init__(self, name, speed, num_gears):
        super().__init__(name, speed)
        self.num_gears = num_gears  # Unique property for Bicycle

    # Method unique to Bicycle
    def pedal(self):
        pass


class Motorcycle(Vehicle):
    def __init__(self, name, speed, fuel_capacity):
        super().__init__(name, speed)
        self.fuel_capacity = fuel_capacity  # Unique property for Motorcycle

     # Method unique to Motorcycle
    def start_emgine(self):
        pass


class Truck(Vehicle):
    def __init__(self, name, speed, max_load_weight):
        super().__init__(name, speed)
        self.max_load_weight = max_load_weight  # Unique property for Truck

    # Method unique to Truck
    def load_cargo(self):
        pass


class Car(Vehicle):
    def __init__(self, name, speed, fuel_type):
        super().__init__(name, speed)
        self.fuel_type = fuel_type  # Unique property for Car

    # Method unique to Car
    def refuel(self):
        pass


class Bus(Vehicle):
    def __init__(self, name, speed, passenger_capacity):
        super().__init__(name, speed)
        self.passenger_capacity = passenger_capacity  # Unique property for Bus

    # Method unique to Bus
    def board_passenger(self):
        pass
