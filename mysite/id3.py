import id3reader
import urllib

mp3 = urllib.urlopen('http://www.moteldemoka.com/moka/somethinggood.mp3')
#i tried using urlopen within the reader but it doesn't work

#id3r = id3reader.Reader('crystalCastles_papSmear[soGoldEDIT].mp3')
#track_title = mp3.getValue('title')
#artist_name = mp3.getValue('performer')
#print artist_name, '-', track_title
