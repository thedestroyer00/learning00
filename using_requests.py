import requests

url = "https://jsonplaceholder.typicode.com/posts?fbclid=IwAR3A_xykcwgXJojhpivW2S4WCLMiZJxTkkhyLmiAi0ZPd20C6unYIyovLlk"

f = open('title.txt', 'w')
r = requests.get(url)
data = r.json()
for index,item in enumerate(data):
    f.write(item['title' ]+ '\n')
    if index == 2:
        break
    
    
f.close()
    
