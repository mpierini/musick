import id3reader
import urllib
import players.models as models

from django.core.management import setup_environ
from mysite import settings

setup_environ(settings)



sample_url = "http://www.moteldemoka.com/moka/somethinggood.mp3"
# mp3 = urllib.urlopen('http://www.moteldemoka.com/moka/somethinggood.mp3')

def add_new_file(url):
	existing_mp3 = models.Song.objects.filter(url = url)
	if existing_mp3:     # There's already this song in the db
		return
	mp3 = urllib.urlopen(url)
	output = open('test.mp3','wb')
	output.write(mp3.read())
	output.close()
	id3r = id3reader.Reader('test.mp3')
	track_title = id3r.getValue('title')
	artist_name = id3r.getValue('performer')

	if artist_name == None:
	    artist_name = "UNKNOWN"
	if track_title == None:
	    track_title = "UNKNOWN"

	new_song = models.Song(name = track_title, artist = artist_name, url = url)
	new_song.save()


def main():
	add_new_file(sample_url)


if __name__ == "__main__":
	main()
