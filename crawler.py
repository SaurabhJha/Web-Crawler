from bs4 import BeautifulSoup
import urllib2
from urlparse import urlparse, urljoin

class Bot:
    def __init__(self, url):
        """
        The constructor initializes a Bot object with url and object
        attributes. The object attribute is supposed to be url object after
        it's downloaded. The object attribute is initialized in crawl
        method.

        Examples
        ========
        >>> from crawler import Bot
        >>> Bot('http://www.google.com')

        """
        self.url = url
        self.object = None

    def crawl(self):
        """
        Downloads the webpage addressed by the url attribute. It returns
        redirected url of the downloaded webpage. It also initialises
        the object attribute.

        Examples
        ========
        >>> from crawler import Bot
        >>> c = Bot('http://www.google.com')
        >>> c.crawl()
        'http://www.google.co.in/?gws_rd=cr&ei=aHhhUuaiHcHmswbu4IDoAg'

        """
        url_object = urllib2.urlopen(self.url)
        redirect_url = url_object.geturl()
        self.url = redirect_url
        redirect_object = urllib2.urlopen(self.url)
        self.object = redirect_object
        return self.url

    def link_extractor(self):
        """
        Returns a list of links that are in the webpage addressed by url
        attribute. If links are relative, they are converted to absolute
        links.

        Examples
        ========
        >>> from crawler import Bot
        >>> c = Bot('http://www.aplopio.com')
        >>> c.crawl()
        >>> c.link_extractor()
        ['http://recruiterbox.com', 'http://wimprint.com']

        """
        url_list = []
        self.crawl()
        text = self.object.read()
        soup = BeautifulSoup(text)
        for link in soup.find_all('a'):
            current_url = link.get('href')
            parse_result = urlparse(current_url)
            if not(parse_result.scheme):
                current_url = urljoin(self.url, current_url) #converts a realtive url to an absoulte url
            url_list.append(current_url)
        return url_list

    def filter_links(self, filter_attribute = 1):
        """
        Filters links of web page based if they are of same netloc
        or not. If filter_attribute is set to 1, it will return the
        urls that have same netloc as parent url. If filter_attribute
        is set to 0, it will return the urls that have different urls
        then parent url.

        Examples
        ========
        >>> from crawler import Bot
        >>> b = Bot('http://www.saurabhjha.me')
        >>> b.filter_links(1)
        ['http://www.saurabhjha.me/software.html']

        """
        if filter_attribute != 1 and filter_attribute != 2:
            raise AttributeError('filter_attribute can only be 1 or 2')
        self.crawl()
        result = []
        url_list = self.link_extractor()
        parse_url = urlparse(self.url)
        for link in url_list:
            parse_link = urlparse(link)
            if filter_attribute == 1:
                if parse_link.netloc == parse_url.netloc:
                    result.append(link)
            else:
                if parse_link.netloc != parse_url.netloc:
                    result.append(link)
        return result

    def geturl(self):
        """
        Returns the redirected url of a webpage.

        Warning: Same instance can give different urls depending
        on whether geturl was called before calling the crawl
        method or after that.

        Examples
        ========
        >>> from crawler import Bot
        >>> c = Bot('http://www.yahoo.com')
        >>> c.geturl()
        'http://www.yahoo.com'
        >>> c.crawl()
        'http://in.yahoo.com/?p=us'
        >>> c.geturl()
        'http://in.yahoo.com/?p=us'

        """
        return self.url
