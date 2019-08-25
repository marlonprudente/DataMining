from bs4 import BeautifulSoup
import requests

session = requests.Session()
session.trust_env = False

url = 'https://www.amazon.com.br/Maxwell-Williams-4080331314-Cafeteira-Francesa/dp/B076PQJ63T/ref=sr_1_1'

homePage = session.get(url)

print(homePage.content)


fsaida = open('paginaColetada.html', 'w')

fsaida.write(str(homePage.content))

soup = BeautifulSoup(homePage.content, 'html.parser')

nomeBruto = soup.find("id", {"id":"productTitle"})
preco = soup.find("id", {"id":"price_inside_buybox"})

print(nomeBruto)
print(preco)

##Testando com outro site diferente da Amazon
