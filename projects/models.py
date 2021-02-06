from django.db import models
from datetime import datetime as dt
from certificates.models import Certificate


class Project(models.Model):
    certificate = models.ForeignKey(Certificate, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    type_con = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.BigIntegerField(default=0)
    completion = models.IntegerField()
    km = models.DecimalField(max_digits=5, decimal_places=2)
    hectares = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_completed = models.BooleanField(default=False)
    list_date = models.DateTimeField(default=dt.now, blank=True)

    def __str__(self):
        return self.title
