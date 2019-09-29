
# using csv module to read and write a csv file 

import csv 


with open('names.csv', 'r') as names:
	info = csv.reader(names)
	
	with open('names_backup.csv', 'w') as backup:
		writer = csv.writer(backup, delimiter = ',')
		for data in info:
			writer.writerow(data)
			
			
			
