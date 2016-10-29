import tweepy

configs = {
    'API KEY': 'FcuBGT2E2vSusk6rNlSfSUQCc',
    'API Secret': 'Lp96ATqrEP4rzoUCiZpBw5b7dXFbJoMCONDFwwuDADjL5S43C2',
    'Access token': '791307771924938752-K1ovtmZGXxasV25GAVsScGu5Mhoc5zF',
    'Access token secret': 'yY2GcZxokNenu88kCQ7F6vVXwhgHipElsXEomQi0TWGwX'
}


class TwitterBot:
    def __init__(self, credentials):
        auth = tweepy.OAuthHandler(consumer_key=credentials['API KEY'],
                                   consumer_secret=credentials['API Secret'])
        auth.set_access_token(credentials['Access token'],
                              credentials['Access token secret'])
        self.api = tweepy.API(auth)

    def update_status(self, status):
        self.api.update_status(status)

    def tweets_timeline(self):
        timeline = self.api.user_timeline()

        tweets_list = []
        for tweet in timeline:
            tweets_list.append(tweet.text)
        return tweets_list
tweety = TwitterBot(configs)

print(tweety.tweets_timeline())

status = input('Enter your tweet: ')
tweety.update_status(status)
