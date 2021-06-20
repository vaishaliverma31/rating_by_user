from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class application(models.Model):
    app_name=models.CharField(max_length=120,unique=True)
    overall_rating=models.FloatField(null=True,validators=[MaxValueValidator(0),MinValueValidator(2)],)
    overall_review=models.CharField(max_length=200,null=True,)
    def __str__(self):
        return self.app_name
class user_define(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE)
   rating=models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(1)])
   review=models.CharField(max_length=200)
   app=models.ForeignKey(application,on_delete=models.CASCADE)

   def __str__(self):
       return  self.user