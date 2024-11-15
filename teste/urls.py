from django.urls import path
from .views import CadastroView, LoginAPIView, Home
from rest_framework_simplejwt.views import ( TokenRefreshView,)

urlpatterns = [
    path("cadastro/", CadastroView.as_view(), name="cadastro"),
    path("login/", LoginAPIView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

urlpatterns += [
    path('home/', Home.as_view(), name='home'),
]