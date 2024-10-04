##All api views are here##

#Models
from Account.models import CustomUser
from Quiz.models import Quiz

#Serializers
from Account.serializers import UsernameSerializer
from Quiz.serializers import QuizSerializer

#REST imports
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

#Other imports
import random


#Allow GET, HEAD, OPTIONS
class UserNameViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UsernameSerializer
    lookup_field = 'username'

#Allow GET, HEAD, OPTIONS
class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field = "uuid"

    #For random '__all__'
    @action(detail=False, methods=['get'], url_path='random')
    def random_quiz(self, request):
        quizzes = list(self.queryset)   # 'queryset' is already created as attribute
        if quizzes:
            random_quiz = random.choice(quizzes)
            serializer = self.get_serializer(random_quiz)
            return Response(serializer.data)
        else:
            return Response({'detail': 'No quiz found'}, status=status.HTTP_404_NOT_FOUND)
        

    
    ###For 'difficulty' based random###
    @action(detail=False, methods=["get"], url_path="random-easy")
    def random_easy_quiz(self, request):
        quizzes = list(Quiz.objects.filter(difficulty='easy'))
        if quizzes:
            random_quiz = random.choice(quizzes)
            serializer = self.get_serializer(random_quiz)
            return Response(serializer.data)
        else:
            return Response({'detail': 'No easy quiz found'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=["get"], url_path="random-medium")
    def random_medium_quiz(self, request):
        quizzes = list(Quiz.objects.filter(difficulty='medium'))
        if quizzes:
            random_quiz = random.choice(quizzes)
            serializer = self.get_serializer(random_quiz)
            return Response(serializer.data)
        else:
            return Response({'detail': 'No medium quiz found'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=["get"], url_path="random-hard")
    def random_hard_quiz(self, request):
        quizzes = list(Quiz.objects.filter(difficulty='hard'))
        if quizzes:
            random_quiz = random.choice(quizzes)
            serializer = self.get_serializer(random_quiz)
            return Response(serializer.data)
        else:
            return Response({'detail': 'No hard quiz found'}, status=status.HTTP_404_NOT_FOUND)