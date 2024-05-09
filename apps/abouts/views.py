from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from .models import *
from .serializers import *

class Email_sendingViewSet(ModelViewSet):
    queryset = Email_sending.objects.all()
    serializer_class = Email_sendingSerializer
    permission_classes = (AllowAny,)


class FAQViewSet(ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = (AllowAny,)


class Contact_informationViewSet(ModelViewSet):
    queryset = Contact_information.objects.all()
    serializer_class = Contact_informationSerializer
    permission_classes = (AllowAny,)


class SertificateViewSet(ModelViewSet):
    queryset = Sertificate.objects.all()
    serializer_class = SertificatesSerializer
    permission_classes = (AllowAny,)


class Images_for_multimediaViewSet(ModelViewSet):
    queryset = Images_for_multimedia.objects.all()
    serializer_class = Images_for_multimediaSerializer
    permission_classes = (AllowAny,)


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (AllowAny,)


class Block_of_contactViewSet(ModelViewSet):
    queryset = Block_of_contact.objects.all()
    serializer_class = Block_of_contactSerializer
    permission_classes = (AllowAny,)


class LecturerViewSet(ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    permission_classes = (AllowAny,)


class SampleViewSet(ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer
    permission_classes = (AllowAny, )

class Sending(APIView):
    @swagger_auto_schema(request_body=SendingSerializer,
                        responses={200: "Question was sent"})
    def post(self, request, *args, **kwargs):
        try:
            data = SendingSerializer(data=request.data)
            data.is_valid()
            receiver = Email_sending.objects.all().first()
            send_mail(
                subject="Question from Student",
                message="Вопрос: " + data.validated_data['question'],
                from_email=receiver, #TODO change to univer email
                recipient_list=["asanabdi50@gmail.com", ],
            )
            return Response({"message": "success"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)