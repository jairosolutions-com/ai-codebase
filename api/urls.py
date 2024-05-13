from django.urls import path
from .views import CodeExplainView, UserView, TokenView, Quiz, RandomQuestion, QuizQuestion

app_name='quiz'

urlpatterns = [
    path('users/', UserView.as_view(), name="users"),
    path('tokens/', TokenView.as_view(), name="tokens"),
    path('a/', CodeExplainView.as_view(), name="answer"),
    path('quiz/', Quiz.as_view(), name='quiz'),
    path('r/<str:topic>/', RandomQuestion.as_view(), name='random' ),
    path('q/<str:topic>/', QuizQuestion.as_view(), name='questions' ),

]