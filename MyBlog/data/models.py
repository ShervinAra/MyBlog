from django.db import models


# Create your models here.
class context(models.Model):
	Name=models.CharField(max_length=30)
	Post=models.TextField()
	Subject=models.CharField(max_length=30)
	Date=models.DateField(auto_now=True, auto_now_add=True,)
	Time=models.TimeField(auto_now=True, auto_now_add=True,)
	
	def __unicode__(self):
		return "%s - %s - %s" % (self.Name,self.Post,self.Subject) 
	
