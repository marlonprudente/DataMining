
from bs4 import BeautifulSoup

pagina = '<html><body><p>Bom dia, CSBC!</p></body></html>'
soup = BeautifulSoup(pagina,'html.parser')
print(soup.prettify())


