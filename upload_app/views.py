from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from .models import UserUpload
# Create your views here.

class UploadListView(ListView):
    model = UserUpload
    template_name = 'home.html'
    context_object_name = 'upload'