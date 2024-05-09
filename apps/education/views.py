from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *


class Admission_dateViewSet(ModelViewSet):
    queryset = Admission_date.objects.all()
    serializer_class = Admission_dateSerializer
    permission_classes = (IsAuthenticated, )


class SpecialtieViewSet(ModelViewSet):
    queryset = Specialtie.objects.all()
    serializer_class = SpecialtieSerializer
    permission_classes = (IsAuthenticated, )


class Scholorship_grantViewSet(ModelViewSet):
    queryset = Scholorship_grant.objects.all()
    serializer_class = Scholorship_grantSerializer
    permission_classes = (IsAuthenticated, )


class Courses_programmsViewSet(ModelViewSet):
    queryset = Courses_programms.objects.all()
    serializer_class = Courses_programmsSerializer
    permission_classes = (IsAuthenticated, )


class ScheduleViewSet(ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticated, )