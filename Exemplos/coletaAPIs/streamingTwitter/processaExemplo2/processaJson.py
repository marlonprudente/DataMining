
import simplejson as json

# Arquivo com Tweets
tweets_file = open('saidaColetaStream.txt', "r")

while True:
  
  #le a linha do arquivo
  tweet_json = tweets_file.readline()
  
  if len(tweet_json)==0:
    break

  #remove espacos em branco
  strippedJson = tweet_json.strip()
  
  tweet = ""

  try:
    #converte uma string json em um objeto python
    tweet = json.loads(strippedJson)
  except:
     continue 

  print(tweet['id']) # ID do tweet	
  print(tweet['created_at']) # data de postagem
  print(tweet['text'].encode('utf-8')) # texto do tweet
			  
  print(tweet['user']['id']) # id do usuario que postou
  print(tweet['user']['name']) # nome do usuario
  print(tweet['user']['screen_name']) # nome da conta do usuario 




