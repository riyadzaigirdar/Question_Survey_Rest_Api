from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework import viewsets, mixins, status
from . import serializers, models
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import generics
from rest_framework.response import Response

class QuestionAdminView(viewsets.ModelViewSet):
    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionAdminSerializer
    permission_classes = [IsAdminUser]

class AnswerUserView(generics.ListCreateAPIView):

    serializer_class = serializers.AnswerUserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = serializers.AnswerUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data['candidiate'] == self.request.user:
                if models.Answer.objects.filter(ques=serializer.validated_data['ques'], candidiate = self.request.user):
                    return Response({"error": "You have already answered this question"})
                else:
                    self.create(request, *args, **kwargs)
                    return Response({"success": "Thanks for your response :)"})
            else:
                return Response({"userInvalid": "You can't vote for others!!"})

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return models.Answer.objects.all()
        return models.Answer.objects.filter(candidiate=user)
    

    

    