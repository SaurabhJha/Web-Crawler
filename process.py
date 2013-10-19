from collections import deque

class Seen(list):
    def __init__(self, array = None):
        if (array == None):
            self.array = []
        else:
            self.array = sorted(array)
    def __contains__(self, item):
        if self.index(item) != None:
            return True
        else:
            return False
    def append(self, item):
        self.array.append(item)
        self.array = sorted(self.array)
    def index(self, item):
        return binsearch(item, self.array, 0, len(self.array))


def process(seed_url):
     c = Bot(seed_url)
     print seed_url
     url = c.crawl()
     s = Seen()
     s.append(url)
     for link in c.filter_links(1):
          process(link)
