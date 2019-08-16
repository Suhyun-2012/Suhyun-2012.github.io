import json
import textblob as tb
from textblob import TextBlob
import matplotlib.pyplot as bar
#import matplotlib.pyplot as sca

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
    print(i["text"])
    cloud = tb.TextBlob(i["text"])
    print(cloud.subjectivity)
    print(cloud.polarity)
    s = s + cloud.subjectivity
    p = p + cloud.polarity
    polarity.append(cloud.polarity)
    subjectivity.append(cloud.subjectivity)

a1=s/len(polarity)
a2=p/len(polarity)
print(a1, a2)

#(x, y, c)

bar.scatter(polarity, subjectivity, color = "lightBlue")
bar.title("graph")


#bar.hist(polarity, bins = [-1, -0.5, 0, 0.5, 1], color = "blue")
#bar.title("happy tweets")
#bar.show()

#bar.hist(subjectivity, bins = [-1, 0, 1], color = "red")
#bar.title("subjective tweets")
bar.show()
