from django.db import models

# Create your models here.
class user(models.Model):
	Name=models.CharField(max_length=30)
	Email=models.EmailField()
	Post=models.TextField()
	Subject=models.CharField(max_length=30)
	
