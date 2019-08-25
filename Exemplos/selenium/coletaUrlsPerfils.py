from linkedin_scraper import Person
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import random
import math


options = Options()
#informacoes do browser, como cookies
options.add_argument("user-data-dir=/home/thiago/.config/google-chrome/Default/")


driver = webdriver.Chrome(chrome_options=options)

try:
    driver.get("https://www.linkedin.com/search/results/people/?company=madeiramadeira")         #open the url in selenium
except:
    print ('bad url!')

#para descer a pagina um pouco para carregar todos os elementos que temos interesse
driver.execute_script("window.scrollTo(0, 600)") 

    
# wait for the page to load
#wait = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'ember1520')))


#dorme x segundos, para dar tempo de carregar a pagina e evitar muitas consultas
time.sleep(random.uniform(5.5, 6.5))


# get the page source
page_source = driver.page_source    

#fecha o driver, mas quando estivermos coletando varias paginas podemos manter ativo pra nao precisar abrir o browser novamente
#driver.close()

soup = BeautifulSoup(page_source, "lxml") #grab the content with beautifulsoup for parsing


#numero total de resultados retornados
totalResultsBruto = soup.find("h3",{"class":"search-results__total Sans-15px-black-55% pl5 pt4 clear-both"}) 
#Frase: Showing x results
frase = totalResultsBruto.text
frase = frase.replace("Showing ","")
totalResults = frase.replace(" results","").strip()

print totalResults

totalPaginas = math.ceil(int(totalResults)/10.0)
print totalPaginas


allResultsBruto = soup.find_all("div",{"class":"search-result__info pt3 pb4 ph0"}) 

saida = open("urlsColetadas-madeiraMadeira.txt","w")

print len(allResultsBruto)

for resultBruto in allResultsBruto:
    linkDetails = resultBruto.find("a",{"class":"search-result__result-link ember-view"}) 
    nomeDetails = resultBruto.find("span",{"class":"name actor-name"})
        
        #Usuario nao tem link e precisamos ignora-lo
    if (nomeDetails == None):
        continue
        
    nome = nomeDetails.text
    nome = nome.replace("\n","")
    nome = nome.encode("utf-8")
    
    
    try:
       link = linkDetails['href']
        
    except:
        print "------------------------------------------erro"
        print resultBruto
        
    print str(link)+"\t"+nome+"\n"
    saida.write(str(link)+"\t"+nome+"\n")


#repetindo o processo para as demais paginas
for pageNumber in range(2,int(totalPaginas+1)):
    try:
        #url com o id da pagina
        driver.get("https://www.linkedin.com/search/results/people/?company=madeiramadeira&page="+str(pageNumber))         
    except:
        print ('bad url!')

    #para descer a pagina um pouco para carregar todos os elementos que temos interesse
    driver.execute_script("window.scrollTo(0, 600)") 
    
    time.sleep(random.uniform(6.5, 7.5))
    
    # get the page source
    page_source = driver.page_source    
    soup = BeautifulSoup(page_source, "lxml") #grab the content with beautifulsoup for parsing
    
    allResultsBruto = soup.find_all("div",{"class":"search-result__info pt3 pb4 ph0"}) 

    allLinks = []

    print len(allResultsBruto)

    for resultBruto in allResultsBruto:
        linkDetails = resultBruto.find("a",{"class":"search-result__result-link ember-view"}) 
        nomeDetails = resultBruto.find("span",{"class":"name actor-name"})
        
        #Usuario nao tem link e precisamos ignora-lo
        if (nomeDetails == None):
            continue
        
        nome = nomeDetails.text
        
        nome = nome.replace("\n","")
        nome = nome.encode("utf-8")
        
        
        try:
            link = linkDetails['href']
            
        except:
            print "------------------------------------------erro"
            print resultBruto
            
        print str(link)+"\t"+nome+"\n"
        saida.write(str(link)+"\t"+nome+"\n")
