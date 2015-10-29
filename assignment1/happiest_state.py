import codecs
import sys
import json

scores = {}
states = {}
sentiments = {}

def init():
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

    for state in states:
        scores[state] = 0

    sent_file = open(sys.argv[1])
    for line in sent_file:
        term,score = line.split("\t")
        sentiments[term]=int(score)

def main():
    init()
    tweet_file = open(sys.argv[2])
    for line in tweet_file:
        tweet = json.loads(line)
        if u'text' in tweet and tweet.get('lang','') == 'en':
            # Tweet has text, able to compute sentiment - Do we have location?
            if 'place' in tweet and tweet.get('place',None) != None:
                if tweet.get('place',{}).get('country','') == 'United States':
                    location = tweet.get('place',None).get('full_name')
                    location = str(location)[-2:]
                    #state is location
                    tweetText = tweet[u'text'].encode('utf-8')
                    words = tweetText.split()
                    for word in words:
                        if word in sentiments:
                            scores[location] = scores.get(location, 0) + sentiments[word]

    # reverse sort scores by value
    foo = sorted(scores, key=scores.get, reverse=True)
    print str(foo[0])
    #for bar in foo:
    #    print bar + " "+str(scores[bar])




if __name__ == '__main__':
    main()
