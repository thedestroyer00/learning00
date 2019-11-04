#downloading images using requests and multhreading(concurrent module)

import requests
import random
import concurrent.futures

urls = ["https://images.unsplash.com/photo-1519245659620-e859806a8d3b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80",
"https://images.unsplash.com/photo-1535448580089-c7f9490c78b1?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1180&q=80",
"https://images.unsplash.com/photo-1511919884226-fd3cad34687c?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80",
"https://images.unsplash.com/photo-1552176625-e47ff529b595?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80",
"https://images.unsplash.com/photo-1543854589-fdd815f176e0?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=907&q=80",
"https://images.unsplash.com/photo-1566473965997-3de9c817e938?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80",
"https://images.unsplash.com/photo-1545553708-263d16d1064d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=700&q=80",
"https://images.unsplash.com/photo-1570294646112-27ce4f174e38?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1334&q=80",
"https://images.unsplash.com/photo-1551055590-23ca93c4effa?ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=80",
"https://images.unsplash.com/photo-1570883482089-a3c3f19af2b0?ixlib=rb-1.2.1&auto=format&fit=crop&w=701&q=80"
]

def downloading_image(url):
	r = requests.get(url).content
	name = str(random.randrange(1000))
	full_name = name +'.jpg'
	print('downloading image')
	with open(full_name, 'wb') as file:
		file.write(r)
	return 'image downloaded'
	
with concurrent.futures.ThreadPoolExecutor() as executor:
	img = [executor.submit(downloading_image, url) for url in urls]
	for i in concurrent.futures.as_completed(img):
		print(i.result())






