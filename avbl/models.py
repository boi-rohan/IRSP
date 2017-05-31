from django.db import models
#import numpy as np

# Create your models here.

class Court(models.Model):
    court_location = models.CharField(max_length = 1000, default = '')
    court_id = models.IntegerField()
    is_occupied = models.BooleanField(default = False)
    image_src = models.CharField(max_length = 1000, default = '')

    def __str__(self):
    	return "Court ID = " + str(self.court_id)

    def last_time(self):
    	t = (self.datetimevalue_set.order_by('-pk')[0]).date_time.time()
    	return t

    def last_date(self):
    	d = (self.datetimevalue_set.order_by('-pk')[0]).date_time.date()
    	return d


class DateTimeValue(models.Model):
    court = models.ForeignKey(Court, on_delete = models.CASCADE)
	#date = models.CharField(max_length = 9)
	#time = models.CharField(max_length = 6)
    date_time = models.DateTimeField(auto_now_add=True, blank = True)
    value = models.BooleanField(default = False)
    owner = models.ForeignKey('auth.User', related_name='DateTimeValue', on_delete=models.PROTECT)
    def __str__(self):
		return 'Court ID:' + str(self.court.court_id) + ' | ' + str(self.date_time) #+ ' ' + str(self.time) + ' ' + str(self.value)
