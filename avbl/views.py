from __future__ import unicode_literals
from django.shortcuts import render
from .models import Court, DateTimeValue
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DateTimeValueSerializer

def index(request):
	all_courts = Court.objects.all()
	return render(request, 'avbl/index.html', {'all_courts':all_courts})


def detail(request, court_id):
	court = Court.objects.get(court_id = court_id)
	return render(request, 'avbl/detail.html', {'court':court})


def add_value(request, date, time, rpi_data, court_id):
	court = Court.objects.get(court_id = court_id)
	new_date_time = DateTimeValue(date = date, time = time, value = rpi_data, court = court)
	new_date_time.save()
	court.is_occupied = rpi_data
	court.save()
	return HttpResponse("<h1>added " + date + "    " + time + "    " + rpi_data + "</h1>")

class DateTimeValueList(APIView):

	def get(self, request):
		

	def post(self):
		