

from bs4 import BeautifulSoup

pagina = "<table><tr><td>one</td><td>two</td></tr></table>"
soup = BeautifulSoup(pagina,'html.parser')

allTR = soup.find_all('tr')
print(allTR)

allTD = soup.find_all('td')
print(allTD)


for t in soup.find_all('td'):
  print(t)

for t in soup.find_all('td'):
  print(t.text)
  
  
