import json
import textblob as tb


#pull tweet data out of json file
tweets = open("tweets_small.json", "r")
tweetData = json.load(tweets)
tweets.close()

#create lists for polarity and subjectivity
polarity = []
subjectivity = []


i = 0
for i in tweetData:
    print(tweetData[0]["text"])
    i = +1
