__author__ = 'gary'

import os
import urllib
import soundcloud
import sqlite3
from mutagen.id3 import ID3NoHeaderError
from mutagen.easyid3 import EasyID3

num_of_tracks = -1
mp3_dir = "D:\Music\Poolside.fm"


def download_song(stream_url, track_no, title, artist):
    global num_of_tracks
    global mp3_dir
    song_name = "%s - %s" % (title, artist)
    url = urllib.urlopen(stream_url)
    if url.getcode() == 200:
        track_dir = "%s\%s" % (mp3_dir, song_name + ".mp3")

        # Download track
        urllib.urlretrieve(stream_url, track_dir)

        # Alter mp3 metadata
        try:
            audio = EasyID3(track_dir)
        except ID3NoHeaderError:
            audio = EasyID3()

        audio["title"] = title
        audio["artist"] = artist
        audio.save(track_dir)


def main():
    global num_of_tracks
    global mp3_dir

    client = soundcloud.Client(client_id='e72237107739281ffceb867534efd87c')

    try:
        con = sqlite3.connect('..\..\db.sqlite3')

        cur = con.cursor()
        # cur.execute('SELECT title, artist, scid FROM ListTracks_track')
        cur.execute(
            'SELECT title, artist, scid '
            'FROM ListTracks_track '
            'WHERE date(dateadded) = date(\'now\');'
        )
        all_tracks = cur.fetchall()

        track_no = 1
        num_of_tracks = len(all_tracks)

    except sqlite3.Error, e:
        print "Error %s:" % e.args[0]
        exit(1)

    print "Downloading.."
    for track in all_tracks:
        try:
            song_name = "%s - %s" % (track[0], track[1])
            if not os.path.isfile("%s\%s" % (mp3_dir, song_name + ".mp3")):
                the_track = client.get('/tracks/%s' % track[2])
                stream_url = client.get(the_track.stream_url, allow_redirects=False)
                download_song(stream_url.location, track_no, track[0], track[1])

            print "%d/%d -- %s" % (track_no, num_of_tracks, song_name)
        except:
            pass

        track_no += 1


    print "Download complete!"

if __name__ == "__main__":
    main()
