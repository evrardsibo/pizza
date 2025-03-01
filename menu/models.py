from django.db import models

class Pizza(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    vegetarian = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='pizza/photos', blank=True)

    def __str__(self):
        return self.name
