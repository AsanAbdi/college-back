from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import *
from .serializers import *

class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated, )


class Main_page_newsSerializer(ModelViewSet):
    queryset = Main_page_news.objects.all()
    serializer_class = Main_page_newsSerializer
    permission_classes = (IsAuthenticated, )