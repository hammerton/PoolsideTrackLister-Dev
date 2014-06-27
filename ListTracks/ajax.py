from dajax.core import Dajax
from django.template.loader import render_to_string
from dajaxice.decorators import dajaxice_register
from views import get_pagination_page
from views import get_search_results

@dajaxice_register
def pagination(request, text, p):
    # track_list = get_pagination_page(p)
    track_list = get_search_results(text, p)
    render = render_to_string('trackList.html', {'track_list': track_list})

    dajax = Dajax()
    dajax.assign('#pagination', 'innerHTML', render)
    return dajax.json()

@dajaxice_register
def search_for_track(request, text):
    track_list = get_search_results(text)
    print track_list
    render = render_to_string('trackList.html', {'track_list': track_list})

    dajax = Dajax()
    dajax.assign('#pagination', 'innerHTML', render)
    return dajax.json()
