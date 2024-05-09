from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerialier
    permission_classes = (IsAuthenticated, )