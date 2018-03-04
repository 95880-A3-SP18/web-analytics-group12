from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.views.generic import ListView

class TodoItem(models.Model):
    item_text = models.CharField(max_length=200)
    def __str__(self):
        return self.item_text
class House(models.Model):
    houseId=models.IntegerField(default=0,primary_key=True)
    month=models.IntegerField(default=1,validators=[MaxValueValidator(12), MinValueValidator(1)])
    bedroom=models.IntegerField(default=1,validators=[MaxValueValidator(7), MinValueValidator(1)])
    distance=models.CharField(max_length=30,default='NA')
    def __str__(self):
        return self.houseId
class Post(models.Model):
    text=models.TextField()
    def __str__(self):
        return self.text[:200]

