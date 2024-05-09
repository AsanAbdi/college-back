from rest_framework import serializers
from .models import *


class Admission_dateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission_date
        fields = "__all__"


class SpecialtieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialtie
        fields = "__all__"


class Scholorship_grantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scholorship_grant
        fields = "__all__"


class Courses_programmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses_programms
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = "__all__"