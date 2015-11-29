import google, urllib2, re, operator
from bs4 import BeautifulSoup

def getQuery(query):
    pages = google.search(query,start=0,stop=10)
    q = findQuery(query.lower())
    names = {}
    for p in pages:
        try:
            url = urllib2.urlopen(p)
        except:
            continue
        page = url.read().decode('ascii', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        pnames = []
        if(q == 1):
            list(map(lambda n: pnames.extend(list(findNames(n))), soup.find_all(string = re.compile('[A-Z][a-z]+ [A-Z][a-z]+'))))
        elif(q == 2):
            list(map(lambda n: pnames.extend(list(findDates(n))), soup.find_all(string = re.compile('((?:(?:January|February|March|April|May|June|July|August|September|October|November|December) (?:[1-3]?[1-9], )?)?[1-9]{4})'))))
        elif(q == 3):
            list(map(lambda n: pnames.extend(list(findPlaces(n))), soup.find_all(string = re.compile('(?:[0-9]+ [A-Z][a-z]+)|(?:[A-Z][a-z]+)|(?:[0-9]+ [A-Z][a-z]+ [A-Z][a-z]+)|(?:[A-Z][a-z]+ [A-Z][a-z]+)|(?:[A-Z][a-z]+, [A-Z][a-z]+)|(?:[A-Z][a-z]+ [A-Z][a-z]+, [A-Z][a-z]+)'))))
        for n in pnames:
            if(n in names):
                names[n] += 1
            else:
                names[n] = 1
    sortedNames = sorted(names.items(), key = lambda x: x[1], reverse = True)
    #print names[sortedNames[0][0]]
    return sortedNames[0][0]
            
def findNames(name):
    pattern = re.compile('[A-Z][a-z]+ [A-Z][a-z]+')
    return pattern.findall(name)

def findDates(date):
    pattern = re.compile('((?:(?:January|February|March|April|May|June|July|August|September|October|November|December) (?:[1-3]?[1-9], )?)?[1-9]{4})')
    return pattern.findall(date)

def findPlaces(place):
    pattern = re.compile('(?:[0-9]+ [A-Z][a-z]+)|(?:[A-Z][a-z]+)|(?:[0-9]+ [A-Z][a-z]+ [A-Z][a-z]+)|(?:[A-Z][a-z]+ [A-Z][a-z]+)|(?:[A-Z][a-z]+, [A-Z][a-z]+)|(?:[A-Z][a-z]+ [A-Z][a-z]+, [A-Z][a-z]+)')
    return pattern.findall(place)

def findQuery(q):
    if q.find("who") > -1:
        return 1
    elif q.find("when") > -1:
        return 2
    elif q.find("where") > -1:
        return 3

#print getQuery("Who plays Spiderman?")
#print getQuery("Where is the Empire State Building")
#print getQuery("When were the Americas discovered?")

