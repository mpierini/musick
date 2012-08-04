#extracting mp3s with beautiful soup
#have been extracting from mostly homepages except for this example

import urllib
from bs4 import BeautifulSoup

soup = BeautifulSoup(urllib.urlopen('http://www.discoworkout.com/?p=3177'))

for link in soup.find_all('a'):
    url = link.get('href')
    if '.mp3' in url:
        print url


