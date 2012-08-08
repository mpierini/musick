#extracting mp3s with beautiful soup
#have been extracting from mostly homepages except for this example

import urllib
from bs4 import BeautifulSoup

blogs = ['http://www.moteldemoka.com', 'http://www.iguessimfloating.com', 'http://www.music.for-robots.com', 'http://www.3hive.com', 'http://www.unpianomusic.com', 'http://www.20jazzfunkgreats.co.uk/wordpress/', 'http://www.gimmetinnitus.com', 'http://www.undertheradarmag.com/media/', 'http://www.mustard-relics.com', 'http://www.xlr8r.com/mp3', 'http://www.fluxblog.org']

for each in blogs:
    soup = BeautifulSoup(urllib.urlopen(each))
    for link in soup.find_all('a'):
        url = link.get('href')
	if '.mp3' in url:
	    #print url
      
           #for each in soup.stripped_strings:
	        #print (repr(each))





