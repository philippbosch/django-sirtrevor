from django.db import models
from sirtrevor.fields import SirTrevorField


class Content(models.Model):
    content = SirTrevorField()
