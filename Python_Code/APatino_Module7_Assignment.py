# Problem 1

class Rectangle:
    # Initializes a new instance of Rectangle with default values
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
    # Generates and returns a description of the rectangle

    def description(self):
        # Return a formatted string containing details of the rectangle
        return f"Name: {self.name}, Coordinates (x, y): ({self.x}, {self.y}), Width: {self.width}, Height: {self.height}, Area: {self.area()}"

     # Updates the coordinates of the rectangle to new values
    def change_coords(self, new_x, new_y):
        self.x = new_x  # Updates the x-coordinate
        self.y = new_y  # Updates the y-coordinate
        # Print confirmation of updated coordinates
        print(f"Coordinates updated to ({self.x}, {self.y})")


# Problem 2

# Problem 3

# Problem 4
