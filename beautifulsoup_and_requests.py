from bs4 import BeautifulSoup
import requests 

url = 'https://coreyms.com'
response = requests.get(url).text

soup = BeautifulSoup(response, 'lxml')

articles = soup.find_all('article')

for article in articles:
	link = article.find(class_ = 'entry-title-link')['href']

	print(link)


