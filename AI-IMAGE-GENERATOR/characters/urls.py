from django.urls import path
from characters import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("characters/", views.CreateCharacterView.as_view(), name="character"),
    path("signup/",views.SignupView.as_view(), name="signup"),
    path("signin/",LoginView.as_view(), name="signin"),
    path("logout/",views.logout_view, name="logout"),
    path("",views.IndexView.as_view(), name="index") 
]



