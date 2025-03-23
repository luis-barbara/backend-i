from django.urls import path
from characters import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("signin/", views.CustomLoginView.as_view(), name="signin"),
    path("select-character/", views.create_character, name="select_character"),
    path("",views.IndexView.as_view(), name="index") 
]



