from rest_framework import serializers
from .models import Court, DateTimeValue


class DateTimeValueSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source = 'owner.username')

	class Meta:
		model = DateTimeValue
		fields = ('date_time', 'value', 'court', 'owner')


class CourtSerializer(serializers.ModelSerializer):

	class Meta:
		model = Court
		fields = ('court_location', 'court_id', 'is_occupied')
