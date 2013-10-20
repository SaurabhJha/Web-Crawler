from crawler import Bot
from collections import deque
from urlparse import urlparse
import urllib2

class Process:
     """
     This is a crawler process, also known as worker thread. It simulates the
     process of taking a seed url and crawling from there. The basic attributes
     of Process are

     seen -> contains a list of urls that have been downloaded. A python list
     fronier -> contains a list of urls that have been discovered but are yet
     to be downloaded.
     harvest -> Web pages that are downloaded.

     """
     def __init__(self):
          self.seen = []
          self.frontier = deque()
          self.harvest = []

     def run(self, url):
          """
          Performs the actual crawling. Takes a seed url as an argument and
          performs a downloading of that url and extracts links on that webpage.
          Then it downlaods the webpages addressed by the links on the previous
          webpage.

          In summary, it performs a breadth first search from the seed url.

          """
          if url in self.seen:
               url = self.frontier.popleft()
          b = Bot(url)
          try:
               downloaded_url = b.crawl()
          except AttributeError:
               url = self.frontier.popleft()
               b = Bot(url)
               downloaded_url = b.crawl()
          except urllib2.URLError:
               url = self.frontier.popleft()
               b = Bot(url)
               downloaded_url = b.crawl()
          print downloaded_url
          self.seen.append(downloaded_url)
          self.harvest.append(downloaded_url)
          current_links = b.link_extractor()
          for link in current_links:
               self.frontier.append(link)
          while len(self.frontier) != 0:
               link = self.frontier.popleft()
               self.run(link)
               
