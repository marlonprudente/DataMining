from linkedin_scraper import Person
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import random
import json



options = Options()
#informacoes do browser, como cookies
options.add_argument("user-data-dir=/home/thiago/.config/google-chrome/Default/")
    
driver = webdriver.Chrome(chrome_options=options)

fileURLs = open("urlsColetadas-madeiraMadeira.txt","r")

saida = open("infoPerfils-madeiraMadeira.txt","w")


while True:
    line = fileURLs.readline()
    if len(line) == 0:
       break
    
    array = line.split("\t")
    link = array[0]
    
    dicUser = {}
    
    try:
        driver.get("https://www.linkedin.com"+str(link))         #open the url in selenium
    except:
        print link
        print ('bad url!')
    
    
    # wait for the page to load
    wait = WebDriverWait(driver, 40)
    driver.execute_script("window.scrollTo(0, 1600)") 
    
    import time
    #dorme x segundos, para dar tempo de carregar a pagina e evitar muitas consultas
    time.sleep(random.uniform(8.5, 9.5))
   
    # get the page source
    page_source = driver.page_source    

    
    #fecha o driver, mas quando estivermos coletando varias paginas podemos manter ativo pra nao precisar abrir o browser novamente
    #driver.close()
    
    
    soup = BeautifulSoup(page_source, "lxml") #grab the content with beautifulsoup for parsing


    nomeUserBruto= soup.find("h1",{"class":"pv-top-card-section__name Sans-26px-black-85%"}) 
    nome = nomeUserBruto.text.encode("utf-8")
    dicUser.update({"nome":nome})

    cidadeBruta= soup.find("h3",{"class":"pv-top-card-section__location Sans-17px-black-70% mb1 inline-block"}) 
    cidade = cidadeBruta.text.encode("utf-8")
    dicUser.update({"cidade":cidade})
    
    nomeEscolaProfileBruto = soup.find( "h3",{"class":"pv-top-card-section__school pv-top-card-section__school--with-separator Sans-17px-black-70% mb1 inline"})
    nomeEscolaProfile = nomeEscolaProfileBruto.text.encode("utf-8")
    nomeEscolaProfile = nomeEscolaProfile.replace("\n","")
    nomeEscolaProfile = nomeEscolaProfile.strip()
    dicUser.update({"nomeEscolaProfile":nomeEscolaProfile})
     
     
    dicUser.update({"link":str(link)})
    
    #Corte de partes que contem educacao do user
    primeiroCorte = soup.find("section",{"class":"pv-profile-section education-section ember-view"})
    segundoCorte = primeiroCorte.find_all("div",{"class":"pv-entity__summary-info"}) 

    listEscolas = []
    
    for conteudoSlice in segundoCorte:
        
        #Parte com o nome da escola
        nomeEscolaBruto = conteudoSlice.find("h3",{"class":"pv-entity__school-name Sans-17px-black-85%-semibold"})
                                                            
        
        #para eliminar infos que nao relacionadas a educacao, pois se nao tem o nome da escola a parte cortada era sobre outra coisa
        if (nomeEscolaBruto == None):
            print link
            print "nao tem o nome da escola"
            continue

        #Pega informacoes do degree, primeira parte do nome
        degreeParte1 = ""
        degreeParte2 = ""
        
        degreeParte1Bruto = conteudoSlice.find("p",{"class":"pv-entity__secondary-title pv-entity__degree-name pv-entity__secondary-title Sans-15px-black-85%"})
        if (degreeParte1Bruto != None):
            degreeParte1 = degreeParte1Bruto.find("span",{"class":"pv-entity__comma-item"}) 
            
       
        #Segunda parte do degree
        degreeParte2Bruto = conteudoSlice.find("p",{"class":"pv-entity__secondary-title pv-entity__fos pv-entity__secondary-title Sans-15px-black-70%"})
        if (degreeParte2Bruto != None):
            degreeParte2 = degreeParte2Bruto.find("span",{"class":"pv-entity__comma-item"}) 
            
        
        dicEscola = {}
        
        
        nomeEscola = nomeEscolaBruto.text.encode("utf-8")
        
        try:
            degreeParte1 = degreeParte1.text.encode("utf-8")
        except:
            print link
            print "erro - continuando 1"
            
        try:    
            degreeParte2 = degreeParte2.text.encode("utf-8")
        except:
            print link
            print "erro - continuando 2"
            
        dicEscola.update({"nomeEscola":nomeEscola})
        dicEscola.update({"degreeParte1":degreeParte1})
        dicEscola.update({"degreeParte2":degreeParte2})
        
        listEscolas.append(dicEscola)
        
        allTime = conteudoSlice.find_all("time")
        count = 1
        for time in allTime:
            dicEscola.update({"time"+str(count):time.text})
            count = count +1
        
        
    dicUser.update({"escolas":listEscolas})
    

    jsonDicUser = json.dumps(dicUser)
    print jsonDicUser
    saida.write(str(jsonDicUser)+"\n")
    
