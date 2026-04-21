#!python3
"""
NOTE:
If you complete this extension, call your teacher over to have it assessed


Create a program to determine the solutions for a quadratic equation
in the format ax^2 + bx + c = 0
A key is the discriminant: b^2 - 4 * a * c
If the discriminant is negative, there are no solutions
If the discriminant is zero, there is only 1 solution
If the discriminant is positive, there are 2 solutions

If the discriminant is a perfect square, then the equation can
be factored

If the discriminant is non zero, the solutions are:
x = (-b + sqrt(b^2 - 4 * a * c)) / 2a
x = (-b - sqrt(b^2 - 4 * a * c)) / 2a

Assignment criteria:
Create a program that inputs 3 float values: a, b, c
function numSolutions(a,b,c) returns an integer with the number of solutions
function solutions(a,b,c) returns a tuple with the solutions (note that if 1 solution,
then both solutions will be the same)

If there are no solutions:
output is: "There are no real solutions"

If there is one solution:
output is "There is 1 solution, x=??"

If there are two solutions:
output is: "The solutions are x=?? and x=??"
"""
import math
def numSolutions(a: float,b: float,c: float):
    # inputs:
    # float a
    # float b
    # float c
    # Description: returns an integer with the number of solutions based off of the discriminates with number of solutions
    #
    # return 0, 1 or 2
    discriminate = b**2 - 4 * a * c
    discriminate = isinstance(discriminate,float)
    discriminate = int(discriminate)
    if discriminate < 0:
        return 0
    elif discriminate == 0:
        return 1
    elif discriminate > 0:
        return 2
    else:
        return 2
        


def solutions(a: float,b: float,c: float):
    #inputs:
    # float a
    # float b
    # float c
    # Desription: finding both x values if the discriminate is a non zero
    #
    # return tuple of float solution1 and float solution2
    discriminate = b**2 - 4 * a * c
    if discriminate < 0:
        return()
    elif discriminate == 0:
        x = -1*b / 2*a
        return(x,x)
    else:
        sqrt_disc = math.sqrt(discriminate)
        x1 = (-1*b + math.sqrt(b**2 - 4 * a * c)) / (2*a)
        x2 = (-1*b - math.sqrt(b**2 - 4 * a * c)) / (2*a)
        return (x1,x2)

def title():
    # inputs none
    # return str of All the title and instructions on one line
    instructions = print("This program will use the function numSolutions(a,b,c) to find the discriminate and the number of solutions there are. Then in the solutions(a,b,c) you are solving using the quadratic formula if they the number of solutions are non zeros. ")
    return instructions


def main():
    # Display Title and Instructions
    print( title() )
    # Your code and function calls should go here
    print(numSolutions(1,6,8))
    print(solutions(1,6,8))


main()