from django.db import models

# Create your models here.

class Recipes(models.Model):
    recipe_name=models.CharField(max_length=100,null=False, blank=False)
    recipe_dec=models.TextField(max_length=200)
    recipe_img=models.ImageField(upload_to='recipeimg/',blank=True,null=True)
