from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

PRODUCT_CATEGORIES = (
		("Vozila", "Vozila"),
		("Namještaj", "Namještaj"),
		("Bela tehnika", "Bela tehnika"),
		("Odjeća", "Odjeća"),
		("Tehnologija", "Tehnologija"),
		("Igračke", "Igračke"),
		("Literatura", "Literatura"),
		("Nekretnine", "Nekretnine"),
		("Ostalo", "Ostalo"),
	)

PRICE_CHOICES = (
		("Iznos", "Iznos"),
		("Po dogovoru", "Po dogovoru"),
	)


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	price = models.CharField(max_length=11, choices=PRICE_CHOICES)
	price_int = models.IntegerField(blank=True, null=True)
	category = models.CharField(choices=PRODUCT_CATEGORIES, max_length=12)
	description = models.TextField(max_length=300)
	post_date = models.DateTimeField(auto_now_add=True)
	img = models.ImageField(blank=True, null=True)
	replacement = models.BooleanField()

	def __str__(self):
		return self.title

class Question(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.CharField(max_length=100)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	post_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.text


