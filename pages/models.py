from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image1 = models.ImageField(upload_to="images/%y/%m/%d")
    image2 = models.ImageField(upload_to="images/%y/%m/%d")
    category = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    description = models.TextField()
    flavor = models.CharField(max_length=200)
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-price']

class Contact(models.Model):
    nom = models.CharField(max_length=50)
    email = models.CharField(max_length=75)
    message = models.CharField(max_length=1010)

    def __str__(self):
        return self.nom
