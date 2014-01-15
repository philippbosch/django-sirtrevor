from django.db import models
from sirtrevor.fields import SirTrevorField


class Content(models.Model):
    headline = models.CharField(max_length=100)
    content = SirTrevorField()
