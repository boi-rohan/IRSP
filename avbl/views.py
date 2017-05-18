from django.shortcuts import render
from django.http import HttpResponse
from .models import Court, Table
#import numpy as np
# Create your views here.

def index(request):
    return HttpResponse("<h1>avlb app homepage</h1>")


def detail(request, court_id):
    return HttpResponse("<h1>This is court number :  " + str(court_id) + "</h1>")

def apnd_table(request, time, rpi_data, court_pk):
	court = Court.objects.get(pk = court_pk)
	table = court.table_set.get(pk = 1)
	#np.vstack((table.abc, np.array([time, rpi_data])))
	table.apnd_value(time, rpi_data)
	table.save()
	court.is_occupied = rpi_data
	court.save()
	return HttpResponse("<h1>appended</h1>")