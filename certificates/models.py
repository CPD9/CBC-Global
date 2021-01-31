from django.db import models
from datetime import datetime as dt

class Certificate(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=50, blank=True)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=dt.now, blank=True)
    def __str__(self):
        return self.name
