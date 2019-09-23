#bubble_sort in python 

def bubble_sort(list):

    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1]= temp




list = [2,6,7,9,1,5]
bubble_sort(list)
print(list)
