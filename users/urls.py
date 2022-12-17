from django.urls import path
from .views import RegisterView,LoginView, UserView

urlpatterns = [
    path('signup', RegisterView.as_view()),
    path('signin', LoginView.as_view()),
    path('user', UserView.as_view()),
]