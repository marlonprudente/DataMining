# -*- encoding: utf-8 -*-

import urllib

#url obtida através do tweet
url = "http://www.utfpr.edu.br"

pagina = urllib.urlopen(url).read()

print(pagina)

fsaida = open('paginaColetada.html','w')
fsaida.write(str(pagina))


