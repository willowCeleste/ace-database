from django.conf import settings
from django.db import models
from django.utils import timezone

class Park(models.Model):
  title = models.CharField(max_length=200)
  created_date = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.title

class Coaster(models.Model):
  title = models.CharField(max_length=200)
  park = models.ForeignKey(Park, on_delete=models.CASCADE, null=True)
  date_opened = models.DateField(null=True)
  incomplete_date_opened = models.CharField(max_length=200, null=True)
  park_string = models.CharField(max_length=200, null=True)

  def __str__(self):
    return self.title