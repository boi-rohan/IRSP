from django.db import models
#import numpy as np

# Create your models here.

class Court(models.Model):
    court_location = models.CharField(max_length = 1000, default = '')
    court_id = models.IntegerField()
    is_occupied = models.BooleanField(default = False)
    image_src = models.CharField(max_length = 1000, default = '')

    def __str__(self):
    	return "Court ID = " + str(self.court_id) + " | " + str(self.is_occupied)

    def last_time(self):
    	t = (self.datetimevalue_set.order_by('-pk')[0]).time
    	return t[0:2]+':'+t[2:4]+':'+t[4:6]

    def last_date(self):
    	d = (self.datetimevalue_set.order_by('-pk')[0]).date
    	return d[0:2]+'/'+d[2:4]+'/'+d[4:6]


class DateTimeValue(models.Model):
	court = models.ForeignKey(Court, on_delete = models.CASCADE)
	date = models.CharField(max_length = 9)
	time = models.CharField(max_length = 6)
	value = models.BooleanField(default = False)

	def __str__(self):
		return 'Court ID:' + str(self.court.court_id) + ' | ' + str(self.date) + ' ' + str(self.time) + ' ' + str(self.value)