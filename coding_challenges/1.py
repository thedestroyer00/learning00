#problem: 
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#solution: 

def findnums(nums, s):
    d = {}
    for i,num in enumerate(nums):
        n = s - num
        if num not in d:
            d[n] = i
        else:
            print([d[num],i])



nums =[3,3]
s = 6
findnums(nums,s)
