# Problem
#we are given 2D coordinates of following points (0,1), (2,4), (3,6), and (7,7).

#1. Store following data in python and write a function to determint distance between two points.
#1. Write a function to estimate polar coordinate of any point.
#1. Write a function that moves point and determines new position when movement is given
import math
p1={"x":0,"y":1}
p2={"x":2,"y":4}
p3={"x":3,"y":6}
p4={"x":7,"y":7}
p5={"x":1,"y":0}
p6={"x":5,"y":0}

print(p1["x"])
def distance(p1,p2):
    x1=p1["x"]
    x2=p2["x"]
    y1=p1["y"]
    y2=p2["y"]
    d=((x2-x1)^2 + (y2-y2)^2)**(1/2)
    return d;

def polar(p1):
    x=p1["x"]
    y=p1["y"]
    phi =math.degrees (math.atan2(y,x))
    return(r,phi)
#distance between two points 
print(distance(p4,p3))

print(polar(p1))