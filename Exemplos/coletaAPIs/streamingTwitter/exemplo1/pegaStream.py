from TwitterAPI import TwitterAPI

twitter_api = TwitterAPI(consumer_key='xxxxxx',
              consumer_secret='xxxxxx',
              access_token_key='xxxxxx',
              access_token_secret='xxxxxx')

filters = {"track": ["impeachment"]}

stream = twitter_api.request('statuses/filter', filters).get_iterator()


for item in stream:
    try:
      print item['text']
    except:
      continue
