from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Information(models.Model):
    Info_name= models.CharField(max_length=100)
    Info_desc= models.CharField(max_length=100)

class Education(models.Model):
    Degree=models.CharField(max_length=50)
    University=models.CharField(max_length=60)
    Score=models.DecimalField(max_digits=4, decimal_places=2)
    Year_passing=models.IntegerField()

class Work_Experience(models.Model):
    duration=models.CharField(max_length=20)
    Name=models.CharField(max_length=50)
    Description=models.CharField(max_length=150)
    Image=models.ImageField(upload_to='media')

class Skills(models.Model):
    skill_name=models.CharField(max_length=30)
    skill_prcnt=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])



class Contact(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50, blank=False, unique=True )
    phone=models.IntegerField()
    Message=models.CharField(max_length=250)