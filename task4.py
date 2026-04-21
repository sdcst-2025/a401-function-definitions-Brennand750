#! python3
"""
Create a function called isInteger()
Input is a float number
Return True if the number is an integer
Return False if the number is not an integer
(2 points)
"""
# create function called isInteger
def isInteger(data):
    # Input is a float
    # Return True if number is an integer
    # Return False is number is not an integer
    if isinstance(data, float):
       return data.is_integer()
    elif isinstance(data, int):
       return True
    else:
       return False
    

if __name__ == "__main__":
  assert isInteger( 9.5 ) == False
  assert isInteger( -2 ) == True    
  assert isInteger("hello") == False
  assert isInteger(0) == True
