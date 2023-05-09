from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Category_Tag(models.Model):
  name = models.CharField(max_length=40)

  def __str__(self):
      return self.name

class RecipeDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    category = models.ManyToManyField(Category_Tag, blank=True)
    description = models.TextField(null=True, blank=True)
    ingredientList = models.TextField(default='Item1')
    introduction = models.TextField(default='Take a bowl.')
    image = models.ImageField(upload_to='images',null=True,blank=True)
    video = models.FileField(upload_to='videos/', null=True, verbose_name="Video",blank=True)
    createdTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['createdTime']


