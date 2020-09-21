from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from users.models import Profile
# Create your models here.

class Question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ques_text=models.CharField(max_length=100)
    pub_date=models.DateTimeField(auto_now_add=True)

    choice1_bool=models.BooleanField(default=False)
    choice1_text=models.CharField(max_length=50)
    choice1_vote=models.IntegerField(default=0)

    choice2_bool=models.BooleanField(default=False)
    choice2_text=models.CharField(max_length=50)
    choice2_vote=models.IntegerField(default=0)

    choice3_bool=models.BooleanField(default=False)
    choice3_text=models.CharField(max_length=50)
    choice3_vote=models.IntegerField(default=0)

    choice4_bool=models.BooleanField(default=False)
    choice4_text=models.CharField(max_length=50)
    choice4_vote=models.IntegerField(default=0)

    def __str__(self):
        return self.ques_text

class RandomImage(models.Model):
    img=models.ImageField(upload_to='images')

class CheckBox(models.Model):
    text_val=models.CharField(max_length=100, blank=True)
    bool_val=models.BooleanField(default=False)
