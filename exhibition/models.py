from django.db import models
from place.models import Place


class Exhibition(models.Model):
    exhibition_id = models.BigIntegerField(primary_key=True)
    exhibition_name = models.CharField(max_length=192, blank=True)
    exdate = models.DateField(null=True, blank=True)
    place = models.ForeignKey(Place)
    direction = models.CharField(max_length=60, blank=True)
    exhibition_description = models.CharField(max_length=792, blank=True)

    class Meta:
        db_table = u'exhibition'

    def __unicode__(self):
        return self.exhibition

