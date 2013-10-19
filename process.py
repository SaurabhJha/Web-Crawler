from crawler import Bot
from collections import deque
from urlparse import urlparse
import urllib2

class Process:
     """
     This is a crawler process, also known as worker thread. It takes
     a seed url and  crawls from there. The basic attributes of Process are

     url -> seed url
     seen -> contains a list of urls that have been downloaded. A python list
     fronier -> contains a list of urls that have been discovered but are yet
     to be downloaded.
     harvest -> Web pages that are downloaded.

     """
     def __init__(self, url):
          self.url = url
          self.seen = []
          self.frontier = deque()
          self.harvest = []

     def run(self, custom_url = None):
          """
          Performs the actual crawling. Comes with an optional argument
          If an explicit url is specified, the run takes that url as
          seed.
          """
          if custom_url == None:
               current_url = self.url
          else:
               current_url = custom_url
          b = Bot(current_url)
          try :
               downloaded_url = b.crawl()
          except AttributeError:
               current_url = self.frontier.popleft()
               downloaded_url = b.crawl()
          except urllib2.URLError:
               current_url = self.frontier.popleft()
               downloaded_url = b.crawl()               
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
               
