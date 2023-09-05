from django.db import models


class TimeStampAbstract(models.Model):
    class Meta:
        abstract = True

    create_at = models.DateTimeField(editable=False, auto_now_add=True)
    update_at = models.DateTimeField(editable=False, auto_now=True)
