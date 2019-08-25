from TwitterAPI import TwitterAPI

twitter_api = TwitterAPI(consumer_key='xxxxxxxx',
              consumer_secret='xxxxxxxx',
              access_token_key='xxxxxxxx',
              access_token_secret='xxxxxxxx') 


r = twitter_api.request('statuses/home_timeline', {'count':5})

for item in r.get_iterator():
    if 'text' in item:
        print item['text']

