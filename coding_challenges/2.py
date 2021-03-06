#Problem: 
#   Given an array of integers, return a new array such that each element at index i of 
#   the new array is the product of all the numbers in the original array except the one at i.
#   For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
#   If our input was [3, 2, 1], the expected output would be [2, 3, 6].


#Solution: 
import copy
from functools import reduce 
def findprod(nums):
	prod = []
	for i in nums:
		dumlist = copy.deepcopy(nums)
		dumlist.remove(i)
		p = reduce((lambda x,y: x*y), dumlist)
		prod.append(p)
	print(prod)


nums = [1, 2, 3, 4, 5]
findprod(nums)
