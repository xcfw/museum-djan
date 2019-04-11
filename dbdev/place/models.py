from django.db import models


class Place(models.Model):
    place_id = models.BigIntegerField(primary_key=True)
    place_name = models.CharField(max_length=180, blank=True)
    address = models.CharField(max_length=180, blank=True)

    class Meta:
        db_table = u'place'
