import lxml.html
import json

"""
1. Scrape Billboard
 - Song's name
 - Singer
 - Weeks on chart
2. Search song's name in YouTube
 - YouTube fingerprint of a song
3. combine above
 - [{'song':'name', 'singe':'name', 'weeks':int, 'fingerprint':'fp'}, ...]
3. encoder as json object
"""
#top1-10
s = "http://www.billboard.com/charts/hot-100"
doc = lxml.html.parse(s)
hot100 = []
rank = 1
for node in doc.xpath("//article/header"):
    hot = {}
    hot['song'] = ''.join(node.xpath("h1/text()")).strip()
    hot['singer'] = ''.join(node.xpath("p/a/text()")).strip()
    hot['weeks'] = int(''.join(node.xpath("ul/li[3]/text()")).strip())
    hot['peak'] = int(''.join(node.xpath("ul[@class='chart_stats']/li[1]/text()")).strip())
    hot['rank'] = rank
    rank += 1
    hot100.append(hot)

#top11-100
for i in range(1, 10):
    s = "http://www.billboard.com/charts/hot-100?page=" + str(i)
    doc = lxml.html.parse(s)
    for node in doc.xpath("//article/header"):
        hot = {}
        hot['song'] = ''.join(node.xpath("h1/text()")).strip()
        hot['singer'] = ''.join(node.xpath("p/a/text()")).strip()
        hot['weeks'] = int(''.join(node.xpath("ul/li[3]/text()")).strip())
        hot['peak'] = int(''.join(node.xpath("ul[@class='chart_stats']/li[1]/text()")).strip())
        hot['rank'] = rank
        rank += 1
        hot100.append(hot)
#YouTube fingerprints
f = open('track/kw20140503.txt', 'wb')
for hot in hot100:
    y = "http://www.youtube.com/results?search_query=" + hot['song'].replace(' ', '+')
    doc = lxml.html.parse(y)
    hot['fingerprint'] = ''.join(doc.xpath("//div/a/@href")[2]).replace('/watch?v=', '')
    print hot['fingerprint']
    f.write(hot['fingerprint'] + '\n')
f.close()

#encoder as json
j = json.dumps(hot100)
fjson = open('track/20140503.json', 'wb')
print >> fjson, j
fjson.close()
