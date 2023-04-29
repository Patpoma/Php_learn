import tweepy, os # secrets in environment variables
def fetch_tweets_from_user(user_namee):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'], os.environ['TWITTER_API_SECRET'])
    auth.set_access_token(os.environ['TWITTER_ACCESS_TOKEN'], os.environ['TWITTER_ACCESS_TOKEN_SECRET'])
    # Create API object
    api = tweepy.API(auth)
    # Create a tweet
    #api.update_status("Hello Tweepy")
    # Create a tweet with media
    #api.update_with_media("image.png", "Hello Tweepy")
    # Create a tweet with media and a location
    #api.update_with_media("image.png", "Hello Tweepy", lat=37.77493, long=-122.41942)
    # Fetch tweets from a user
    tweets = api.user_timeline(screen_name=user_namee, count=5)
    # Create a list of tweet information
    tweets_for_csv = [tweet.text for tweet in tweets] # CSV file created
    for j in tweets_for_csv:
        print(j)
    return tweets_for_csv