from django.db import models

# Create your models here.

class Court(models.Model):
    court_location = models.CharField(max_length = 1000)
    court_id = models.IntegerField()
    is_occupied = models.BooleanField(default = False)


    def __str__(self):
    	return "Court ID = " + str(self.court_id) + " | " + str(self.is_occupied)

