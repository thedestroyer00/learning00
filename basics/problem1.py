'''
input -> list1 = [2,3,4,7,9,10,12,14,15,16,18]
output -> 
[2, 3, 4]
[9, 10]
[14, 15, 16]
'''

# if any other easier method then please suggenst me

list1 = [2,3,4,7,9,10,12,14,15,16,18]
output = []
sub = []

j =0
for i in range(1,len(list1)):
    if list1[j] not in sub:
        sub.append(list1[j])
    
    if list1[i]-1 == sub[len(sub)-1]:
        sub.append(list1[i])
        j+=1
        
    else:
        j=i
        if (len(sub)> 1):
            output.append(sub)
            sub =[]
        else:
            sub = []

for i in output:
    print(i)
