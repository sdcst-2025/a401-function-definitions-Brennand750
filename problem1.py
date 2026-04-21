#!python3
""" 
Create a function called hypotenuse()
Input is 2 float numbers and a boolean
If the boolean is True, then find the hypotenuse
If the boolean is False, then the larger number is the hypotenuse
Return the missing side

assert hypotenuse(3,4,True) == 5
(2 points)
"""
import math
def hypotenuse(a:float, b:float, calculate:bool):
    # input 2 float numbers and a boolean
    # If boolean is true, find hypotenuse
    # If boolean is false, then the larger number is the hypotenuse
    if calculate:
        return math.sqrt(a**2 + b**2)
    else:
        hypo = max(a,b)
        leg = min(a,b)
        if hypo >= leg:
            return math.sqrt(hypo**2 - leg**2)
    

if __name__ == "__main__":
    assert hypotenuse(3,4,True) == 5
    assert hypotenuse(5,12,True) == 13
    assert hypotenuse(3,5,False) == 4
    assert hypotenuse(13,12,False) == 5
    
    