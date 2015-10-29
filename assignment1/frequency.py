import sys
import json

# Initialise a dictionary of frequencies
terms = {}
allWords = 0
# Open the tweet file
tweet_file = open(sys.argv[1])
for line in tweet_file:
    tweet = json.loads(line)
    if u'text' in tweet:
        tweetText = tweet[u'text'].encode('utf-8')
        words = tweetText.split()
        for word in words:
            if len(word) > 0:
                allWords = allWords + 1
                if word in terms:
                    terms[word] = terms[word] + 1
                else:
                    terms[word] = 1

# Print frequencies
for term in terms.items():
    print term[0] + " " + "{:.8f}".format(float(term[1])/float(allWords))

