from django.shortcuts import render
from .models import *

# def home(req):
#     return render(req, 'app/index.html')

from django.views.generic import ListView

class HomeListView(ListView):
    template_name = 'app/index.html'
    model = Post
    import markdown    
