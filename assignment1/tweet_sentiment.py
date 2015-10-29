import json
import sys

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = {}
    for line in sent_file:
        term,score = line.split("\t")
        scores[term] = int(score)

    for line in tweet_file:
        tweet = json.loads(line)
        if u'text' in tweet:
            tweetText = tweet[u'text'].encode('utf-8')
            words = tweetText.split(" ")
            score = 0
            for word in words:
                if word in scores:
                    score = score + scores[word]
            print str(score)

if __name__ == '__main__':
    main()
