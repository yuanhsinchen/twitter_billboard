"""
scrape_youtube.py
"""

import lxml.html

filename = 'keywords_0412.txt'
f = open(filename, 'r')
keywords = f.readlines()

#s = "http://www.youtube.com/results?search_sort=video_view_count&search_query="
s = "http://www.youtube.com/results?search_query="
top100 = []
for keyword in keywords:
    print keyword
    doc = lxml.html.parse(s+keyword.replace(" ", "+"))
    top100.append(doc.xpath("//div/a/@href")[2])

    
"""
doc = lxml.html.parse(s)
top100 = doc.xpath("//header/h1/text()")
top100 = [s.strip() for s in top100]
top100s = doc.xpath("//header/p/a/text()")
top100s = [s.strip() for s in top100s]
"""
"""
#top11-100
for i in range(1, 10):
    s = "http://www.billboard.com/charts/hot-100?page=" + str(i)
    doc = lxml.html.parse(s)
    top = doc.xpath("//header/h1/text()")
    top = [s.strip() for s in top]
    for s in top:
        top100.append(s)

    tops = doc.xpath("//header/p/a/text()")
    tops = [s.strip() for s in tops]
    for s in tops:
        top100s.append(s)

top100 += top100s
%0A"""

f = open('urls.txt', 'w+')
for s in top100:
    print s
    f.write(s + '\n')
f.close()

#print top100
