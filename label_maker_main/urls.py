from django.urls import path
from .views import Home

app_name = 'label_maker'

urlpatterns = [
    path('', Home.as_view(), name='home'),
]