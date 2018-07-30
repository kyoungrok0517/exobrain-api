from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class Triple(models.Model):
    uid = models.CharField(max_length=200)
    sbj = JSONField()
    rel = JSONField()
    obj = JSONField()
    source = JSONField()
    context = models.CharField(max_length=200)

    def __str__(self):
        return self.uid

    class Meta:
        ordering = ('uid',)
