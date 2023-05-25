from bs4 import BeautifulSoup
import requests

sitioweb = 'https://parascrapear.com/'
respuesta = requests.get(sitioweb)
content = respuesta.text

soup = BeautifulSoup(content, 'lxml')
print(soup.prettify())