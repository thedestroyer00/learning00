#Mulit threating in python

from threading improt Thread
from time import sleep 


class world(Thread):
	def run(self):
		for i in range(5):
			print("The world")
			sleep(1)
			
			
			
class beauty(Thread):
	def run(self):
		print("is beautiful")
		sleep(1)
		
		
w = world()
b = beauty()

w.run()
sleep(0.3)
b.run()

w.join()
b.join()

print("As a whole - The world is beautiful")
