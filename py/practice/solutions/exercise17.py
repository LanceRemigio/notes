import requests
from bs4 import BeautifulSoup

url = 'https://www.github.com/'

r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html)

title = soup.find('span', 'articletitle')
print(title)

