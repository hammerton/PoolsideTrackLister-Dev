from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
from django.db.models import Q
from ListTracks.AppCode.TrackService import TrackService
from ListTracks.models import Track

# Create your views here.
def home(request):
    # http://www.dajaxproject.com/
    # https://docs.djangoproject.com/en/1.6/topics/pagination/
  	# http://thecodeplayer.com/walkthrough/javascript-css3-calculator
  	# http://thenextweb.com/creativity/2014/06/21/key-color-harmony-avoiding-boredom-chaos/

    #  AJAX Searching
    # https://www.djangopackages.com/packages/p/django-autocomplete-light/
    # https://www.djangopackages.com/packages/p/django-selectable/
    # http://stackoverflow.com/questions/6674062/implement-an-ajax-search-in-django
    # http://django-ajax-search.readthedocs.org/en/latest/index.html
    # https://github.com/crucialfelix/django-ajax-selects
    # http://jqueryui.com/autocomplete/

    t = TrackService()
    t.insertNewTracks()

    return render(request, 'index.html', { })

def get_search_results(text="", page=1):

    if text != "":
        track_list = Track.objects.all().filter(
            Q(title__contains=text) | Q(artist__contains=text)
        )
    else:
        track_list = Track.objects.all().order_by('dateadded')

    paginator = Paginator(track_list, 3)

    try:
        page = int(page)
    except ValueError:
        page = 1

    try:
        track_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        track_list = paginator.page(paginator.num_pages)

    return track_list
