import requests 

url = "https://jsonplaceholder.typicode.com/posts?fbclid=IwAR3A_xykcwgXJojhpivW2S4WCLMiZJxTkkhyLmiAi0ZPd20C6unYIyovLlk"

r = requests.get(url)
data = r.json()

load_data = {}

for index, info in enumerate(data):
	load_data[index] = info
	
	
print(load_data)	
	

