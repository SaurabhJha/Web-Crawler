from crawler import Bot
from collections import deque
from urlparse import urlparse

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

     def run(self, url = None):
          """
          Performs the actual crawling. Comes with an optional argument
          If an explicit url is specified, the run takes that url as
          seed.
          """
          if url == None:
               url = self.url
          if url in self.seen:
               return None
          b = Bot(url)
          redirect_url = b.crawl()
          print redirect_url #for tracking purposes
          self.harvest.append(redirect_url)
          self.seen.append(redirect_url)
          links = b.link_extractor()
          for l in links:
               parse_result = urlparse(l)
               self.frontier.append(l)
          for l in self.frontier:
               self.run(l)
