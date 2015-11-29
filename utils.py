import google, urllib2, re, operator
from bs4 import BeautifulSoup

def getQuery(query):
    pages = google.search(query,start=0,stop=10)
    names = {}
    for p in pages:
        try:
            url = urllib2.urlopen(p)
        except:
            continue
        page = url.read().decode('ascii', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        pnames = []
        if(query.split()[0].lower() == 'who'):
            list(map(lambda n: pnames.extend(list(findNames(n))), soup.find_all(string = re.compile('[A-Z][a-z]+ [A-Z][a-z]+'))))
        elif(query.split()[0].lower() == 'when'):
            list(map(lambda n: pnames.extend(list(findDates(n))), soup.find_all(string = re.compile('((?:(?:January|February|March|April|May|June|July|August|September|October|November|December) (?:[1-3]?[1-9], )?)?[1-9]{4})'))))
        for n in pnames:
            if(n in names):
                names[n] += 1
            else:
                names[n] = 1
    sortedNames = sorted(names.items(), key = lambda x: x[1], reverse = True)
    print names[sortedNames[0][0]]
    return sortedNames[0][0]

def findNames(name):
    pattern = re.compile('[A-Z][a-z]+ [A-Z][a-z]+')
    return pattern.findall(name)

def findDates(date):
    pattern = re.compile('((?:(?:January|February|March|April|May|June|July|August|September|October|November|December) (?:[1-3]?[1-9], )?)?[1-9]{4})')
    return pattern.findall(date)

print getQuery("Who plays Spiderman?")
print getQuery("When were the Americas discovered?")

