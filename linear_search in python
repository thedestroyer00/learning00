#linear search in python 
def search(list, num):

    l = 0
    u = len(lst)

    m = (l + u) // 2
    a = 1

    while a < 2:

        if num == list[m]:
            print(num, "index is ", m )
            a += 1
        elif list[m] < num:
            l = m
            m = (l+u)//2
        elif list[m] > num:
            u = m
            m = (l+u)//2



lst = [3, 25, 65, 6, 4, 7, 8, 45, 87, 12, 56, 78, 90, 49, 97]
lst.sort()


num = int(input("enter an number"))


if num in lst:
    search(lst, num)
else:
    print("the number doesn't exist in the list")

	
