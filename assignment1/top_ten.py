import sys
import json

hashtags = {}
allHash = 0

def main():
    allHash = 0
    tweet_file = open(sys.argv[1])
    for line in tweet_file:
        tweet = json.loads(line)
        if tweet.get('entities','') != '' and tweet.get('entities','').get('hashtags','') != '':
            tweettags = tweet.get('entities','').get('hashtags','')
            for h in tweettags:
                hashtags[h.get('text')] = hashtags.get(h.get('text'),0) + 1
                allHash = allHash + 1

    foo=sorted(hashtags, key=hashtags.get, reverse=True)
    for count in range(0,10):
        print foo[count].encode('utf-8') + " " + str(hashtags[foo[count]])

if __name__ == '__main__':
    main()

