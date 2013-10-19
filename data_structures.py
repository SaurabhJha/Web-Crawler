from tools import binsearch

class Seen(list):
    """
    Data structure used to keep a list of url that have been
    downloaded. It's attribute is a sorted list named as array.

    """
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
