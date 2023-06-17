from django.db import models
import uuid
# Create your models here.
# class Client(models.Model):
#     nom = models.CharField(max_length=20)
#     prenom = models.CharField(max_length=20)
#     telephone = models.CharField(max_length=20)
#     whatsapp = models.CharField(max_length=20)
#     email = models.CharField(max_length=20)
#     adresse = models.CharField(max_length=20)
#     ville = models.CharField(max_length=20)
#     pays = models.CharField(max_length=20)
#     def __str__(self):
#         return self.nom + ' ' + self.prenom
    
# class Order(models.Model):
#     client_name = models.CharField(max_length=30)
#     products = models.CharField(max_length=10000)
#     price = models.DecimalField(max_digits=20,decimal_places=2)
#     state = models.BooleanField()
#     def __str__(self):
#         return self.client_name
    
class Order(models.Model):
    order_id=models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    telephone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=20)
    pays = models.CharField(max_length=20)
    ids = models.CharField(max_length=2000)
    products = models.CharField(max_length=10000)
    price = models.DecimalField(max_digits=20,decimal_places=2)
    delivered = models.BooleanField(default=False)
    def __str__(self):
        return self.nom + ' ' + self.prenom
    