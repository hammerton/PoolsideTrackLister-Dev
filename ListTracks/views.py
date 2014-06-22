import soundcloud
import json
import urllib2
from django.shortcuts import render
from ListTracks.AppCode.TrackService import TrackService
from ListTracks.models import Track

# Create your views here.

def home(request):
  # http://www.pythonforbeginners.com/python-on-the-web/parsingjson/
  # http://poolsideapi2.herokuapp.com/tracks
  # http://stackoverflow.com/questions/6578986/how-to-convert-json-data-into-a-python-object
  # http://stackoverflow.com/questions/4528099/convert-string-to-json-using-python
  # http://www.siteground.com/tutorials/siteground-git/clone-git-repository.htm

#   # create a client object with your app credentials
#   client = soundcloud.Client(client_id='e72237107739281ffceb867534efd87c')
  
#   response = urllib2.urlopen('http://poolsideapi2.herokuapp.com/tracks')
#   tracks = json.loads(response.read())
  
#   for t in tracks[:3]:
#       try:
#         embed_info = client.get('/oembed', url=t['scUrl'])
# #         print embed_info.__getattr__('html')
#         t['embedHtml'] = embed_info.__getattr__('html')
#       except:
#         pass
      
#   return render(request, 'index.html', {'tracks': tracks})

  t = TrackService()
  t.insertNewTracks()
  
  tracks = Track.objects.all()[:10]
  return render(request, 'index.html', {'tracks': tracks})





