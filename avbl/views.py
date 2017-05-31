from __future__ import unicode_literals
from django.shortcuts import render
from .models import Court, DateTimeValue
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .serializers import DateTimeValueSerializer, CourtSerializer
from .permissions import IsOwnerOrReadOnly

def index(request):
	all_courts = Court.objects.all()
	return render(request, 'avbl/index.html', {'all_courts':all_courts})


def detail(request, court_id):
	court = Court.objects.get(court_id = court_id)
	return render(request, 'avbl/detail.html', {'court':court})


def add_value(request, date, time, rpi_data, court_id):
	court = Court.objects.get(court_id = court_id)
	new_date_time = DateTimeValue(value = rpi_data, court = court)
	new_date_time.save()
	court.is_occupied = rpi_data
	court.save()
	return HttpResponse("<h1>added " + date + "    " + time + "    " + rpi_data + "</h1>")


class CourtList(APIView):
#/api/
	def get(self, request, format = None):
		all_courts = Court.objects.all()
		serializer = CourtSerializer(all_courts, many = True)
		return Response(serializer.data)

'''
class DateTimeValuePost(APIView):
#/api/post_datetimevalue/
	def post(self, request, format = None):
		serializer = DateTimeValueSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
'''



class DateTimeValueList(generics.ListCreateAPIView):
	queryset = DateTimeValue.objects.all()
	serializer_class = DateTimeValueSerializer

	def perform_create(self, serializer):
		serializer.save(owner = self.request.user)

	permission_classes = (permissions.IsAuthenticatedOrReadOnly,
							IsOwnerOrReadOnly,)



class DateTimeValueDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = DateTimeValue.objects.all()
	serializer_class = DateTimeValueSerializer
	permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
