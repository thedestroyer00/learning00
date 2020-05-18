#Problem
#Given an array of integers, find the first missing positive integer in linear time and constant space.
#In other words, find the lowest positive integer that does not exist in the array. 
#The array can contain duplicates and negative numbers as well.
#For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

def find_missing(arr):
  arr.sort()
  great = arr[-1]
  for i in range(1,great+2):
    if i not in arr:
      print(i)
      break
    else:
      pass


arr = [-1,30,23,2,1,0,4,5,6,8,10,11,3]
find_missing(arr)
