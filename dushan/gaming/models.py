from django.db import models

# Create your models here.

# class StoreItemDes:  #create a class to create objects for each item in the store list and assign new values to it
#     discount: int
#     image: str
#     price: int
#     description:str
#     id:int                #before creating a postgres database using this class


class StoreItemDes(models.Model):  # after creating a postgres database using this class
    # creating the table(class) and its fields(columns) using the class and its attributes
    discount = models.IntegerField()
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    description = models.CharField(max_length=50)


class StoreNewGamesSlide(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    rating = models.FloatField()
    price = models.IntegerField()
    category = models.CharField(max_length=50)    
