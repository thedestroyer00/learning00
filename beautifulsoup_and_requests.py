from bs4 import BeautifulSoup
import requests 

url = 'https://coreyms.com'
response = requests.get(url).text

soup = BeautifulSoup(response, 'lxml')

article = soup.find('article')

link = article.find(class_ = 'entry-title-link')['href']

print(link)


