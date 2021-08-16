from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Conveyance(models.Model):
	
	Date=models.CharField(max_length=50)
	From_Location=models.CharField(max_length=50)
	To_Location=models.CharField(max_length=50)
	Conveyance_Date=models.CharField(max_length=20)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	Amount=models.IntegerField()
	Remark=models.TextField()

	image=models.ImageField(upload_to='events/',default='',blank=True)
	RemarkAdmin=models.CharField(max_length=200,blank=True,default='')
	Status=models.BooleanField(default=False)

	def __str__(self):
		return self.Remark



class Holiday(models.Model):
	
	Date=models.CharField(max_length=50)
	Day=models.CharField(max_length=50)
	Occasion=models.CharField(max_length=50)


	def __str__(self):
		return self.Occasion


class Post(models.Model):
	Topic=models.CharField(max_length=50)
	Date=models.DateTimeField(auto_now_add=True)
	Author=models.CharField(max_length=50)
	Info=models.TextField()


	def __str__(self):
		return self.Author


class Notice(models.Model):
	Date=models.DateTimeField(auto_now_add=True)
	Topic=models.CharField(max_length=50)
	Info=models.TextField()


	def __str__(self):
		return self.Topic