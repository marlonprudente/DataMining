

import requests
from bs4 import BeautifulSoup


##pagina porcao Fourquare

url="https://www.amazon.com.br/Maxwell-Williams-4080331314-Cafeteira-Francesa/dp/B076PQJ63T/ref=sr_1_1"

##retorna o conteudo da pagina
req = requests.get(url)

##transforma o conteudo da pagina em um objeto BeautifulSoup
soup = BeautifulSoup(req.content,'html.parser')

nomeBruto = soup.find("span",{"id":"productTitle"})


print nomeBruto.text





