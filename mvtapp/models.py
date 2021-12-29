from django.db import models

# Create your models here.
class webdevelopment_details(models.Model):
	did=models.CharField(primary_key=True,max_length=20)
	name=models.CharField(max_length=20)
	age=models.IntegerField()
	phone_no=models.IntegerField(unique=True)
	gender=models.CharField(max_length=20)

	class Meta:
		verbose_name='webdevelopment_details'
		verbose_name_plural='webdevelopment_detailss'

	def __star__(self):
		return self.name
