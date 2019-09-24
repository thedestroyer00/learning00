#using python to download an image from web

import random 
import urllib.request

def download(url):
	name = random.randrange(10000)
	full_name = str(name) + ".jpg"
	urllib.request.urlretrieve(url, full_name)
	
	
download("url of image")
	
