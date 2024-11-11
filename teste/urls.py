from django.urls import path
from .views import CadastroView, LoginAPIView, ExampleView
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView,)

urlpatterns = [
    path("cadastro", CadastroView.as_view(), name="cadastro"),
    path("login", LoginAPIView.as_view()),
    path('ok/', ExampleView.as_view(), name='ok'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
