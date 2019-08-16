import json
import textblob as tb
from textblob import TextBlob


#pull tweet data out of json file
tweets = open("tweets_small.json", "r")
tweetData = json.load(tweets)
tweets.close()

#create lists for polarity and subjectivity
polarity = []
subjectivity = []


s=0
p=0
a1=0
a2=0
for i in tweetData:
    print(tweetData[0]["text"])
    cloud = tb.TextBlob(i["text"])
    print(cloud.subjectivity)
    print(cloud.polarity)
    s = s + cloud.subjectivity
    p = p + cloud.polarity
    polarity.append(cloud.polarity)

a1=s/len(polarity)
a2=p/len(polarity)
print(a1, a2)
