import json, sys
reload(sys)
sys.setdefaultencoding("utf-8")

def main():
    parsetweets()

def parsetweets():
    f = open('../data/test.20140408-210403.json')

    track = []
    url = open('urls_0412.txt')
    for line in url:
        track.append(line.strip('\n'))
    url.close()

    f1 = open('fp.txt', 'w')

    url_tweet = {}
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
    for i in track:
        if i in url_tweet:
            f1.write(i)
            f1.write('\n')
            url_tweet[i] = url_tweet[i].replace('\n', ' ')
            f1.write(url_tweet[i])
            f1.write('\n')

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
