from django.db import models

# Create your models here.


class User(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=32)
    profile_photo=models.ImageField(upload_to="profile_images/")
    description=models.TextField(default="")

    def __str__(self):
        return self.first_name


#http://localhost:8000/media/profile_images/photo.jpg
