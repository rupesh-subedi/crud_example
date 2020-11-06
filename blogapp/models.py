from django.db import models


# Create your models here.
class Post(models.Model):
	Title = models.CharField(max_length=500)
	description = models.TextField(max_length=500)

	def __str__(self):
		return f"{self.Title}-{self.description}"
