from bs4 import BeautifulSoup
import urllib2
from urlparse import urlparse, urljoin

class Crawl:
    def __init__(self, url):
        self.url = url
        self.object = None

    def crawl(self):
        url_object = urllib2.urlopen(self.url)
        redirect_url = url_object.geturl()
        self.url = redirect_url
        redirect_object = urllib2.urlopen(self.url)
        self.object = redirect_object
        return self.url
            
    def duplicate_checker(self):
        return self.url in Seen

    def link_extractor(self):
        url_list = []
        if not(self.object):
            self.object = urllib2.urlopen(self.url)
        text = self.object.read()
        soup = BeautifulSoup(text)
        for link in soup.find_all('a'):
            current_url = link.get('href')
            parse_result = urlparse(current_url)
            if not(parse_result.scheme):
                current_url = urljoin(self.url, current_url)
            url_list.append(current_url)
        return url_list
