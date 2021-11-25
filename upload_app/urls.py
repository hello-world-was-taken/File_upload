from django.urls import path

urlpatterns = [
    path('', UploadListView.as_view(), name='home'),   
]