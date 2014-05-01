import json, sys
reload(sys)
sys.setdefaultencoding("utf-8")

def main():
    parsetweets()
    #parsehot100()

def parsehot100():
    f = open('track/20140503.json')
    f1 = open('track/20140503.csv', 'wb')

    for line in f:
        line = line.strip()

        try:
            data = json.loads(line)
        except ValueError as detail:
            #sys.stderr.write(detail.__str__() + "\n")
            continue
        for i in range(len(data)):
            f1.write(str(data[i]['fingerprint']))
            f1.write(',')
            f1.write(str(data[i]['song']))
            f1.write(',')
            f1.write(str(data[i]['rank']))
            f1.write(',')
            f1.write(str(data[i]['peak']))
            f1.write(',')
            f1.write(str(data[i]['weeks']))
            f1.write('\n')
    f1.close()

def parsetweets():
    #f = open('../data/test.20140408-210403.json')
    f = open('../data/test.' + sys.argv[1] + '.json')
    url = open(sys.argv[2])
    track = []
    for line in url:
        track.append(line.strip('\n'))
    url.close()

    #file for tweets collection by fingerprint
    f1 = open('features/tweets-' + sys.argv[1] + '.csv', 'w')
    #file for number of sharing in tweets by fingerprint
    f2 = open('features/sharing-' + sys.argv[1] + '.csv', 'w')
    url_tweet = {}
    url_share = {}
    for line in f:
        line = line.strip()

        try:
            data = json.loads(line)
        except ValueError as detail:
            #sys.stderr.write(detail.__str__() + "\n")
            continue
        if data['lang'] == 'en':
            for i in data['entities']['urls']:
                eurl = str(i['expanded_url'])
                tweet =  str(data['text'])
                for fp in track:
                    if fp in eurl:
                        if fp in url_tweet.keys():
                            url_tweet[fp] += ' ' + tweet
                        else:
                            url_tweet[fp] = '' + tweet
                        if fp in url_share.keys():
                            url_share[fp] += 1
                        else:
                            url_share[fp] = 1
    for i in track:
        if i in url_tweet:
            f1.write(i)
            f1.write(',')
            url_tweet[i] = url_tweet[i].replace('\n', ' ').replace(',', ' ')
            f1.write(url_tweet[i])
            f1.write('\n')
        if i in url_share:
            f2.write(i)
            f2.write(',')
            f2.write(str(url_share[i]))
            f2.write('\n')
    f1.close()
    f2.close()

def jsontocsv():
    f = open('../data/test.20140408-210403.json')
    f1 = open('../data/test_output.csv', 'w')
    for line in f:
        line = line.strip()

        data = ''
        try:
            data = json.loads(line)
        except ValueError as detail:
            sys.stderr.write(detail.__str__() + "\n")
            continue
        if data['lang'] == 'en':
            f1.write(str(data['created_at']) + ', ')
            f1.write(str(data['id']) + ', ')
            f1.write(str(data['text']) + ', ')
            f1.write(str(data['user']['id']) + ', ')
            if len(data['entities']['hashtags']) > 0:
                for i in data['entities']['hashtags']:
                    if len(i['text']) > 0:
                        f1.write(str(i['text']) + ', ')
            else:
                f1.write('' + ', ')
            if len(data['entities']['urls']) > 0:
                for i in data['entities']['urls']:
                    if len(i['url']) > 0:
                        f1.write(str(i['url']))
            else:
                f1.write('')
            f1.write('\n')

if __name__ == '__main__':
    main()
