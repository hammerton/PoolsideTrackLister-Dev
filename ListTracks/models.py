from django.db import models
from django.utils.encoding import smart_unicode


# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length=120)
    artist = models.CharField(max_length=120)
    scid = models.CharField(max_length=50)
    scurl = models.CharField(max_length=255)
    twitter = models.CharField(max_length=50)
    _id = models.CharField(max_length=50)
    embedhtml = models.TextField()
    dateadded = models.DateTimeField(auto_now_add = True, auto_now = False)

    def __unicode__(self):
        return smart_unicode(self.title + ' - ' + self.artist)
