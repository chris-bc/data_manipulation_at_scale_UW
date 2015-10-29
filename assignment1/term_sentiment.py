import sys
import json

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}
    terms = {}
    for line in sent_file:
        term,score = line.split("\t")
        scores[term] = int(score)
    
    for line in tweet_file:
        tweet = json.loads(line)
        if u'text' in tweet:
            tweetText = tweet[u'text'].encode('utf-8')
            # Compute score of tweet
            score = 0
            sampledWords = 0
            words = tweetText.split(" ")
            for word in words:
                if word in scores:
                    score = score + scores[word]
                    sampledWords = sampledWords + 1
            
            # Add or update inferred sentiment of words not in scores
            if sampledWords == 0:
                sampledWords = 1
                score = 0
            for word in words:
                if word not in scores:
                    if word in terms:
                        terms[word] = terms[word] + float(score)/sampledWords
                    else:
                        terms[word] = float(score)/sampledWords
            
    for term in terms.items():
        #print term + " " + str(terms[term])
        print term[0] + " " + str(term[1])
        #print terms[term]

if __name__ == '__main__':
    main()
