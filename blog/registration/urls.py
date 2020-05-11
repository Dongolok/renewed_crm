from django.urls import path

from .views import RegistrationAPIView, login
'''LoginAPIView'''

app_name = 'authentication'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    # path('login/', LoginAPIView.as_view()),
    path('login/', login)

]
