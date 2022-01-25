from django.urls import path, include
from user.views import RegisterView, LoginView, LogoutView  

urlpatterns = [
    path('', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout', LogoutView.as_view()),



]
