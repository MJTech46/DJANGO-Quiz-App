##All api views are here##

#Models
from .models import NotePad
from Account.models import CustomUser

#Serializers
from .serializers import NotePadeSerialiser
from Account.serializers import UsernameSerializer

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

