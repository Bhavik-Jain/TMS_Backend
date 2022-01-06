from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50, null=True)
	phone = models.CharField(max_length= 200, null = True)
	dob = models.DateField()
	
	def __str__(self):
		return self.name

class Packages(models.Model):
	STATUS = (
	('Drafts', 'Drafts'),
	('Published', 'Published'),
	)
	name = models.CharField(max_length=50, null=True)
	details = models.CharField(max_length=200, null=True)
	price = models.PositiveIntegerField()
	days = models.CharField(max_length=10, null=True)
	nights = models.CharField(max_length=10, null=True)
	image = models.ImageField(blank=True, null=True)
	status = models.CharField(max_length=200, choices=STATUS, default='Drafts')	
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

class Bookings(models.Model):
	STATUS = (
	('Pending', 'Pending'),
	('Approved', 'Approved'),
	)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	package = models.ForeignKey(Packages,on_delete=models.CASCADE)
	date = models.DateField()
	status = status = models.CharField(max_length=200, choices=STATUS, default='Pending')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user