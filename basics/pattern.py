'''
print the following pattern: 
ASCOL
ASCO
ASC
AS
A
AS
ASC
ASCO
ASCOL
'''

name = "ASCOL"
check = 0
for i in range(10,0, -1):
	if i >= 5:
		for j in range(i-5):
			print(name[j], end = "")
		if i != 5:
			print("\n")

	else : 
		for j in range(6 -i):
			print(name[j], end = '')
		print("\n")
