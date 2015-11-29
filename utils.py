import google, urllib2, re, operator
from bs4 import BeautifulSoup

def getQuery(query):
    pages = google.search(query,start=0,stop=10)
    names = {}
    i = 10
    for p in pages:
        try:
            url = urllib2.urlopen(p)
        except:
            continue
        page = url.read().decode('utf-8')
        soup = BeautifulSoup(page, 'html.parser')
        pnames = soup.find_all(string = re.compile('[A-Z][a-z]+ [A-Z][a-z]+'))
        for n in pnames:
            if(n in names):
                names[n] += 1
            else:
                names[n] = 1 + i
        i-= 1
    sortedNames = sorted(names.items(), key = lambda x: x[1], reverse = True)
    return sortedNames[0][0]

print getQuery("Who plays Spiderman?")

