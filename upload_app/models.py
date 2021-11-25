from django.db import models

# Create your models here.

class UserUpload(models.Model):
    ass_name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='images/')
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.ass_name