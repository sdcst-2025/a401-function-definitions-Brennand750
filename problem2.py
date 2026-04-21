#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math

def distance(coord1:float, coord2:float):
    # Input 2 tuples, that each contain an (x,y) coordinate.
    # return the distance between each coordinate.
    x1 , y1 = coord1
    x2 , y2 = coord2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    

if __name__ == "__main__":
    d = distance( (2,4) , (6,3) )
    assert round(d,3) == 4.123
    d = distance( (-3,2.2) , (1,2))
    assert round(d,3) == 4.005


