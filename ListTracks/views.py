from django.shortcuts import render
from ListTracks.AppCode.TrackService import TrackService
from ListTracks.models import Track


# Create your views here.
def home(request):
    t = TrackService()
    t.insertNewTracks()

    tracks = Track.objects.all()[:10]
    return render(request, 'index.html', {'tracks': tracks})
