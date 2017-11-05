import pickle, urllib2, json, os
def write_to_file(final):
    b = open('final1.txt','wb')
    pickle.dump(final,b)
    b.close()

def read_from_file():
    b = open('final1.txt','rb')
    return pickle.load(b)
    b.close()

def merge_all_files():
    final = []
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for f in files:
        r = f.split('.')
        if r[-1] == 'txt' and r[0] != 'final':
            a = open(f,'rb')
            x = pickle.load(a)
            final.extend(x)
            #print f, ' : ', len(x)
    print '------------------------------------------------'
    a.close()
    return final

def complete_incomplete_files(final):
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
    for x in range(len(final)):
        if final[x]['title'] == '':

            y = final[x]['url']['url'].split('/')[-1]

            site = 'http://www.theimdbapi.org/api/movie?movie_id='+y
            req = urllib2.Request(site, headers=hdr)

            try:
                page = urllib2.urlopen(req)
            except urllib2.HTTPError, e:
                print e.fp.read()

            contents = json.loads(page.read())
            print contents['title'], contents['release_date']
            final[x] = contents
    return final
def incomplete_count(final):
    count = 0
    for x in range(len(final)):
        if final[x]['title'] == '':
            count += 1
    return 'Incomplete Entries: '+ str(count)



database = merge_all_files()
print incomplete_count(database)
#write_to_file(database)
#a = read_from_file()
#print incomplete_count(a)
a = complete_incomplete_files(database)
print incomplete_count(a)
write_to_file(a)