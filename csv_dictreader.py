import csv 

with open('names.csv', 'r') as file1 :
 	data = csv.DictReader(file1)
	
	with open('dict_writer', 'w') as file2:
		fields = ['first_name', 'last_name', 'email']
		writer = csv.DictWriter(file2, fields, delimiter = '\t')  # \t means a tab in python 
		writer.writeheader()   #writeheader() is used to writer the field on the first line of the csv file 
		
		for line in data:
			writer.writerow(line)  
