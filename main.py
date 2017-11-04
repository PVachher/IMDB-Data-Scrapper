import json, urllib2,cookielib, pickle

def scraper(start,end):
    a = open(str(start)+'-'+str(end)+'.txt','wb')
    db = []
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}
    for y in range(start,end):
        site = 'http://www.theimdbapi.org/api/movie?movie_id=tt'+str(y)
        req = urllib2.Request(site, headers=hdr)

        try:
            page = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print e.fp.read()

        contents = json.loads(page.read())
        print contents['title'], contents['release_date'], str(y)
        db.append(contents)
    pickle.dump(db,a)
    a.close()
scraper(1700,1800)
scraper(1800,1900)
scraper(1900,2000)
scraper(2000,2100)
scraper(2100,2200)
