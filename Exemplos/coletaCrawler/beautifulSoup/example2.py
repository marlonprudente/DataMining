
from bs4 import BeautifulSoup

pagina = '<html><body><p>Bom dia, CSBC!</p><p>teste</p></body></html>'
soup = BeautifulSoup(pagina,'html.parser')

allP = soup.find_all('p')
print(allP)

print(allP[0])

