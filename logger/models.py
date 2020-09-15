from django.db import models

# Create your models here.
class Temperature(models.Model):
	time = models.DateTimeField()
	temp = models.FloatField()

	def __str__(self):
		return "{}ºC at {}".format(str(self.temp), self.time)
