import urllib2
import json
import soundcloud
from ListTracks.models import Track


class TrackService():
    # http://www.pythonforbeginners.com/python-on-the-web/parsingjson/
    # http://poolsideapi2.herokuapp.com/tracks
    # http://stackoverflow.com/questions/6578986/how-to-convert-json-data-into-a-python-object
    # http://stackoverflow.com/questions/4528099/convert-string-to-json-using-python
    # http://www.siteground.com/tutorials/siteground-git/clone-git-repository.htm

    poolsideTrackListURL = 'http://poolsideapi2.herokuapp.com/tracks'

    def __init__(self):
        # create a client object with your app credentials
        self.client = soundcloud.Client(client_id='e72237107739281ffceb867534efd87c')
        self.new_track_list = []

    def __getEmbedHTML(self, scUrl):
        try:
            embed_info = self.client.get('/oembed', url=scUrl)
            return embed_info.__getattr__('html')
        except:
            return ''

    def insertNewTracks(self):
        response = urllib2.urlopen(TrackService.poolsideTrackListURL)
        tracks = json.loads(response.read())
        for track in tracks[:3]:
            if Track.objects.filter(scid=track['scId']).count() == 0:
                t = Track(
                    title=track['title'],
                    artist=track['artist'],
                    scid=track['scId'],
                    scurl=track['scUrl'],
                    twitter=track['twitter'],
                    _id=track['_id'],
                    embedhtml=self.__getEmbedHTML(track['scUrl'])
                )
                t.save()
                self.new_track_list.append(t)
