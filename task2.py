#!python3
"""
##### Task 2
Create a function called largest.
The input is a list or tuple.
Your function should convert any tuples to lists so that you can sort
it and find the largest.
If you are stuck, don't forget to refer to your assignment on lists to help you sort (or ask Google)
The return value is the largest value in the list
(2 points)
"""
def largest(data):
  # inputs
  # input a list or tuple, and should convert any tuples to list
  # data(list or tuple): input the list or tuple
  # x value to determine if larger number is a float or integer
  # return the largest value in the list
  if isinstance(data, tuple):
    data = list(data)
  return max(data)

if __name__ == "__main__":
  assert largest((3,1,4,7,13,9)) == 13
  assert largest([5,1,12.3]) == 12.3
  assert largest([-3,-1,1.2,0.2]) == 1.2

