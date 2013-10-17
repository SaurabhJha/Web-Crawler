from bs4 import BeautifulSoup
import urllib2

Seen = []
Frontier = []
Harvest = []

class Crawler:
    def __init__(self, url):
        self.url = url

    def crawl(self):
        url_object = urllib2.urlopen(self.url)
        redirected_url = url_object.geturl()
        self.url = redirected_url
        val = uvalue(self.url)
        if val in Seen:
            return False
        redirected_object = urllib2.urlopen(self.url)
        Harvest.append(self.url)
        Seen.append(val)

    def get_links(self):
        redirected_object = urllib2.urlopen(self.url)
        text = redirected_object.read()
        soup = BeautifulSoup(text)
        a_tags = soup.find_all('a')
        for a in a_tags:
            link = a.get('href')
            if not(absolute(link)):
                link = toabsolute(link, self.url)
            Frontier.append(link)

def absolute(url):
    return url[:7] == 'http://'
        
def toabsolute(relative_url, parent_url):
    return parent_url + '/' + relative_url

def uvalue(url):
    length = len(url)
    return  url[12] + url[15] + url[length - 7] + url[length - 5]
