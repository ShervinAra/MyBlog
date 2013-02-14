from django.db import models

# Create your models here.
class context(models.Model):
	Name=models.CharField(max_length=30)
	Email=models.EmailField()
	Post=models.TextField()
	Subject=models.CharField(max_length=30)
	
	def __unicode__(self):
		return (self.Name)
	
