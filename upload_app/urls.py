from django.urls import path
from .views import UploadListView

urlpatterns = [
    path('', UploadListView.as_view(), name='home'),   
]