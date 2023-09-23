from django.db import models

# Create your models here.
class cart(models.Model):
    user = models.CharField(max_length=20)
    product_name = models.CharField(max_length=20)
    count = models.IntegerField(default=1)
    image = models.CharField(max_length=50)
    model_name = models.CharField(max_length=20)
    amount = models.IntegerField()

    def __str__(self):
     return self.image
class order(models.Model):
   user_name = models.CharField(max_length=20)
   country = models.CharField(max_length=20)
   firstname = models.CharField(max_length=30)
   lastname = models.CharField(max_length=20)
   address = models.CharField(max_length=100)
   state = models.CharField(max_length=20)
   postal = models.IntegerField()
   email = models.EmailField(max_length=100)
   phone = models.IntegerField()
   products = models.CharField(max_length=200)
   image = models.CharField(default='media/images/blue.jpg',max_length=40)
   quantity = models.IntegerField(default=1)
   total = models.IntegerField()
   payment = models.CharField(max_length=20)