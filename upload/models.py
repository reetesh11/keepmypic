from __future__ import unicode_literals

from django.db import models

class Photos(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(null=False, default=False, upload_to='photos')

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = "photos"
        ordering = ["-created_at"]

class Thumbnail(models.Model):
    photo = models.ForeignKey(Photos, null=True)
    thumbnail = models.ImageField(upload_to='thumbnail')
