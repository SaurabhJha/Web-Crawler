from crawler import Bot
from data_structures import Seen
from collections import deque

class Process:
     def __init__(self, url):
          self.url = url
          self.seen = Seen()
          self.frontier = deque()
          self.level = 0
          self.harvest = []

     def run(self, url = None):
          if url == None:
               url = self.url
          if url in self.seen:
               return None
          b = Bot(url)
          redirect_url = b.crawl()
          self.harvest.append(redirect_url)
          self.seen.append(redirect_url)
          links = b.link_extractor()
          for l in links:
               self.frontier.append(l)
          for l in self.frontier:
               self.run(l)
