from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters

from .models import *
from .serializers import *

class Email_sendingViewSet(ModelViewSet):
    queryset = Email_sending.objects.all()
    serializer_class = Email_sendingSerializer
    permission_classes = (AllowAny,)
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    search_fields = ["receiver", ]
    filterset_fields = ["receiver", ]


class FAQViewSet(ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = (AllowAny,)
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    search_fields = ["question", "answer"]
    filterset_fields = ["question", "answer"]


class Contact_informationViewSet(ModelViewSet):
    queryset = Contact_information.objects.all()
    serializer_class = Contact_informationSerializer
    permission_classes = (AllowAny,)
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    search_fields = ["title", "type", "text"]
    filterset_fields = ["title", "type", "text"]


class SertificateViewSet(ModelViewSet):
    queryset = Sertificate.objects.all()
    serializer_class = SertificatesSerializer
    permission_classes = (AllowAny,)
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    search_fields = ["title", "description"]
    filterset_fields = ["title", "description"]


class Images_for_multimediaViewSet(ModelViewSet):
    queryset = Images_for_multimedia.objects.all()
    serializer_class = Images_for_multimediaSerializer
    permission_classes = (AllowAny,)
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    search_fields = ["title", "type"]
    filterset_fields = ["title", "type"]

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (AllowAny,)
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    search_fields = ["title", "role", "email", "contact"]
    filterset_fields = ["title", "role", "email", "contact"]

class Block_of_contactViewSet(ModelViewSet):
    queryset = Block_of_contact.objects.all()
    serializer_class = Block_of_contactSerializer
    permission_classes = (AllowAny,)
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    search_fields = ["title", "contact", "email"]
    filterset_fields = ["title", "contact", "email"]

class LecturerViewSet(ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = (AllowAny,)
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    search_fields = ["name", "age", "bio", "subject"]
    filterset_fields = ["name", "age", "bio", "subject"]

class SampleViewSet(ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    permission_classes = (AllowAny, )
    filter_backends = [filters.DjangoFilterBackend, SearchFilter]
    search_fields = ["title", "description"]
    filterset_fields = ["title", "description"]


class Sending(APIView):
    @swagger_auto_schema(request_body=SendingSerializer,
                        responses={200: "Question was sent"})
    def post(self, request, *args, **kwargs):
        try:
            data = SendingSerializer(data=request.data)
            data.is_valid()
            receiver = Email_sending.objects.all().first()
            send_mail(
                subject="Question from Student: " + data.validated_data["name"],
                message="Вопрос: " + data.validated_data['question'] + "\n почта для ответа: " + data.validated_data["email"],
                from_email=receiver,
                recipient_list=[receiver, ], #TODO change to univer email
            )
            return Response({"message": "success"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)