from crawler import Bot

b1 = Bot('http://www.yahoo.com')
b2 = Bot('http://www.aplopio.com')
b3 = Bot('http://www.saurabhjha.me')

#Basic Downloading
assert b1.crawl() == 'http://in.yahoo.com/?p=us'

#Basic Link Extraction without filters
assert b2.link_extractor() == ['http://recruiterbox.com', 'http://wimprint.com']

#Link Extraction with filters
assert b3.filter_links(1) == ['http://www.saurabhjha.me/software.html']
assert b3.filter_links(2) == ['http://gndu.ac.in', 'http://saurabhjhablog.wordpress.com']
