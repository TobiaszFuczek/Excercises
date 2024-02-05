# Skorzystaj z biblioteki BeautifulSoup do pobrania tytułów najnowszych artykułów z dowolnej strony internetowej.
import requests

page_url= 'https://miroslawmamczur.pl/'
page= requests.get(page_url)

print(page)
print(page.content)

from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

list_all_p = soup.find_all('a')
print(f'znalazłem {len(list_all_p)} linków')
list_all_p[10]
list_all_p[10].get_text()
for link in soup.find_all('a'):
    print(link.get('href'))
