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
        self.id = self.api.me().id

    def update_status(self, status):
        self.api.update_status(status)

    def tweets_timeline(self):
        """
        Returns 20 latest tweets of user
        """
        timeline = self.api.user_timeline()
        return [(tweet.text, tweet.id) for tweet in timeline]

    def destroy_status(self, status_id):
        self.api.destroy_status(status_id)

    def send_message_to_followers(self, text):
        for user_id in self.get_followers_ids():
            self.api.send_direct_message(user_id=user_id, text=text)

    def get_followers_ids(self):
        return self.api.followers_ids()

    def get_friends_ids(self):
        return self.api.friends_ids()
