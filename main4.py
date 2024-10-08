# Problem
#we are given 2D coordinates of following points (0,1), (2,4), (3,6), and (7,7).

#1. Store following data in python and write a function to determint distance between two points.
#1. Write a function to estimate polar coordinate of any point.
#1. Write a function that moves point and determines new position when movement is given
import math

# 1. Storing the points in a list of tuples
points = [(0, 1), (2, 4), (3, 6), (7, 7)]

# Function to calculate the Euclidean distance between two points
def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    # Using the Euclidean distance formula
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to convert Cartesian coordinates to polar coordinates
def to_polar(point):
    x, y = point
    # Radius (r) is the distance from the origin to the point
    r = math.sqrt(x ** 2 + y ** 2)
    # Angle (theta) is the angle with respect to the positive x-axis, in radians
    theta = math.atan2(y, x)
    return r, theta

# Function to move a point by a displacement (dx, dy)
def move_point(point, dx, dy):
    x, y = point
    # New position after adding displacement to the original coordinates
    new_x = x + dx
    new_y = y + dy
    return new_x, new_y

# Example usage

# 1. Calculating distance between two points
p1 = points[0]  # (0, 1)
p2 = points[1]  # (2, 4)
print(f"Distance between {p1} and {p2}: {distance(p1, p2)}")

# 2. Converting a point to polar coordinates
polar_p1 = to_polar(p1)
print(f"Polar coordinates of {p1}: (r = {polar_p1[0]}, θ = {polar_p1[1]} radians)")

# 3. Moving a point by a given displacement (dx, dy)
dx, dy = 3, -1
new_position = move_point(p1, dx, dy)
print(f"New position of {p1} after moving by ({dx}, {dy}): {new_position}")
