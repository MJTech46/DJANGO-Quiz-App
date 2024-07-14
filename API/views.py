##All api views are here##

#Models
from .models import NotePad
from Account.models import CustomUser
from Quiz.models import Quiz

#Serializers
from .serializers import NotePadeSerialiser
from Account.serializers import UsernameSerializer
from Quiz.serializers import QuizSerializer

#Other imports
from rest_framework import viewsets, mixins


#Allow __all__
class NotePadeViewSet(viewsets.ModelViewSet):
    queryset = NotePad.objects.all()
    serializer_class = NotePadeSerialiser

#Allow GET, HEAD, OPTIONS
class UserNameViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UsernameSerializer
    lookup_field = 'username'

#Allow GET, HEAD, OPTIONS
class QuizViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field = "uuid"
