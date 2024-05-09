from rest_framework import serializers
from .models import *

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class Main_page_newsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main_page_news
        fields = "__all__"