from django.urls import path, include
from app.views import *
from . import views

app_name = 'app'


urlpatterns = [
path('', HomeListView.as_view(), name='home')
]
