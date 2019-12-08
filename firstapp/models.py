from django.db import models

import os
def upload_app_files(instance, filename):
	ext = filename.split('.')[-1]
	fname = filename.split('.')[-2]
	timestamp = '%d/%m/%Y-%H:%M:%S'
	filename = "%s_%s.%s" % (timestamp, fname, ext)
	return os.path.join('firstapp', filename)

# Create your models here.
class Product(models.Model):

	name = models.CharField(max_length=100)
	img  = models.ImageField(upload_to=upload_app_files,blank=True)
	desc = models.TextField(blank=True)
	price= models.IntegerField()
	offer= models.BooleanField(default=False)

