import json, sys
reload(sys)
sys.setdefaultencoding("utf-8")

def main():
    f = open('../data/test.20140403-023229.json')
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
