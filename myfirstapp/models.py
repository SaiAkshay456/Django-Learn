from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class User(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=32)
    profile_photo=models.ImageField(upload_to="profile_images/")
    description=models.TextField(default="")
    date_to=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name


#http://localhost:8000/media/profile_images/photo.jpg

class UserReview(models.Model):

    userr=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_review')
    rating=models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ])
    description=models.TextField(default="")
    date_to=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.userr.first_name} review for user'
