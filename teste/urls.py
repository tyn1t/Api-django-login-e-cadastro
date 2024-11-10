from django.urls import path
from .views import UserCreateView


urlpatterns = [
    path("cadastro", UserCreateView.as_view(), name="cadastro"),
]

