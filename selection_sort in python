# selection sort of int list in python 


def sort(list,n):

    for i in range(n):
        min_position = i
        for j in range(i, n + 1):
            if list[j] < list[min_position]:
                min_position = j

        temp = list[i]
        list[i] = list[min_position]
        list[min_position] = temp


nums = [5, 4, 6, 3, 8, 7, 9, 1, 2]
n = len(nums) - 1
sort(nums, n)

print(nums)

