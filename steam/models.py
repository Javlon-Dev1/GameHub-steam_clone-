from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)    
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    release_date = models.DateField()
    developer = models.CharField(max_length=100)
    genres = models.ManyToManyField(Genre)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title