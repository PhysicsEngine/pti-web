from django.db import models

# Create your models here.


class Authors(models.Model):
    name = models.CharField(max_length=40)
    rate = models.DecimalField(max_digits=7, decimal_places=3)

class Articles(models.Model):
    title = models.CharField(max_length=255, null=True)
    pub_date = models.DateTimeField()
    url = models.URLField(max_length=511)
    author = models.ForeignKey(Authors)

