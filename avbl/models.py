from django.db import models
#import numpy as np

# Create your models here.

class Court(models.Model):
    court_location = models.CharField(max_length = 1000)
    court_id = models.IntegerField()
    is_occupied = models.BooleanField(default = False)

    def __str__(self):
    	return "Court ID = " + str(self.court_id) + " | " + str(self.is_occupied)


class Table(models.Model):
	abc = []
	court = models.ForeignKey(Court, on_delete = models.CASCADE)

	def __str__(self):
		return str(len(self.abc))

	def apnd_value(self, time, rpi_data):
		self.abc.append([time, rpi_data])