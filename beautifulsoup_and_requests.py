from bs4 import BeautifulSoup
import requests 

url = 'https://github.com'
response = requests.get(url).text

