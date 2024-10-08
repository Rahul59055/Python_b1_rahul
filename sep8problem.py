#(0,1),(2,4),(3,6),and (7,7)

class Point:
    # Constructor to initialize x and y coordinates
    def __init__(self, x, y):  # Fix constructor name
        self.x = x  # Assign x coordinate
        self.y = y  # Assign y coordinate
    
    # Method to return a readable string representation of the object
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

# Initializing the object p1 with (0, 1)
p1 = Point(0, 1)

# Print the object p1
print(p1)  # This will print: Point(0, 1)
