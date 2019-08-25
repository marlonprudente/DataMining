# -*- encoding: utf-8 -*-
from TwitterAPI import TwitterAPI
import simplejson as json

#Um registro no website da API fornece as credenciais indicadas aqui
twitter_api = TwitterAPI(consumer_key='xxxxxxx',
              consumer_secret='xxxxxxx',
              access_token_key='xxxxxxx',
              access_token_secret='xxxxxxx') 

filters = {"track": ["Lava Jato"]} #palavra que deseja buscar em tweets

stream = twitter_api.request('statuses/filter', filters).get_iterator()

fsaida = open('saidaColetaStream.txt','w')

for item in stream:
  itemString = json.dumps(item) #Serialize obj to a JSON formatted str.
  fsaida.write(itemString+'\n')
  
  
  
  
  
  