from django.urls import path
from characters import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("characters/", views.CreateCharacterView.as_view(), name="character"),
    path("characters/create/", views.CreateCharacterView.as_view(), name="character-create"),
    path("characters/list/", views.CharacterListView.as_view(), name="character-list"),
    path("characters/<int:pk>/edit/", views.CharacterUpdateView.as_view(), name="character-edit"),
    path("characters/<int:pk>/delete/", views.CharacterDeleteView.as_view(), name="character-delete"),
    path("signup/",views.SignupView.as_view(), name="signup"),
    path("signin/",LoginView.as_view(), name="signin"),
    path("logout/",views.logout_view, name="logout"),
    path("",views.IndexView.as_view(), name="index") 
]



