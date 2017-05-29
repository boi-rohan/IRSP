from rest_framework import serializers
from .models import Court, DateTimeValue


class DateTimeValueSerializer(serializers.ModelSerializer):

	class Meta:
		model = DateTimeValue
		fields = ('date', 'time', 'value', 'court')
		