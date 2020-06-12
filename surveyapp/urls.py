from django.urls import path, include
from .views import QuestionAdminView, AnswerUserView
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('question', QuestionAdminView)

urlpatterns = [
    path('',include(router.urls)),
    path('qanswer/',AnswerUserView.as_view() )
    
]

 