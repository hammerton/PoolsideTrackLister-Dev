from dajax.core import Dajax
from django.template.loader import render_to_string
from dajaxice.decorators import dajaxice_register
from views import get_pagination_page

@dajaxice_register
def pagination(request, p):
    print "Hello"
    track_list = get_pagination_page(p)
    render = render_to_string('trackList.html', {'track_list': track_list})

    dajax = Dajax()
    dajax.assign('#pagination', 'innerHTML', render)
    return dajax.json()