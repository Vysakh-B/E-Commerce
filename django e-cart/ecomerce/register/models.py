from django.db import models

# Create your models here.
class products(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images')
    model_name = models.CharField(max_length=50)
    product_type = models.CharField(max_length=20)
    price = models.IntegerField()
    gender = models.CharField(max_length=10) 
