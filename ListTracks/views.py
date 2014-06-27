from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from ListTracks.AppCode.TrackService import TrackService
from ListTracks.models import Track


# Create your views here.
def home(request):
    # http://www.dajaxproject.com/
    # https://docs.djangoproject.com/en/1.6/topics/pagination/
	# http://thecodeplayer.com/walkthrough/javascript-css3-calculator
	# http://thenextweb.com/creativity/2014/06/21/key-color-harmony-avoiding-boredom-chaos/
    
    t = TrackService()
    t.insertNewTracks()

    # track_list = Track.objects.all()
    # track_paginator = Paginator(track_list, 10)

    # page = request.GET.get('page')
    # try:
    #     tracksPerPage = track_paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer, deliver first page.
    #     tracksPerPage = track_paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range (e.g. 9999), deliver last page of results.
    #     tracksPerPage = track_paginator.page(track_paginator.num_pages)

    return render(request, 'index.html', {'track_list': get_pagination_page()})

def get_pagination_page(page=1):
    track_list = Track.objects.all()
    paginator = Paginator(track_list, 5)

    print "hello2"

    try:
        page = int(page)
    except ValueError:
        page = 1

    try:
        track_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        track_list = paginator.page(paginator.num_pages)

    return track_list
