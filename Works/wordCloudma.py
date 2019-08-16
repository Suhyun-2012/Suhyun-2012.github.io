import json
from wordcloud import WordCloud
import textblob as tb
from textblob import TextBlob

tweets = open("tweets_small.json", "r")
tweetData = json.load(tweets)
tweets.close()

oneString = ""

for tweets in tweetData:
    oneString = oneString + tweets["text"]
    print(oneString)

#generate words list from wordcloud
twets = TextBlob(oneString)
twetsWordList = twets.words

word_count = {}
#loop thru words list
for words in twetsWordList:
    count = twetsWordList.words.count(words)
    word_count[words] = count
#count loop frequency, create dictionary
