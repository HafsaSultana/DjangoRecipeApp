from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from taggit.managers import TaggableManager
# Create your models here.


class Category_Tag(models.Model):
  name = models.CharField(max_length=60)


  def __str__(self):
      return self.name

class RecipeDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=200)
    category = models.ManyToManyField(Category_Tag)
    description = models.TextField(null=True, blank=True)
    ingredientList = models.TextField(default='Item1')
    introduction = models.TextField(default='Take a bowl.')
    image = models.ImageField(upload_to='images/',null=True,blank=True)
    video = models.FileField(upload_to='videos/', null=True, verbose_name="Video",blank=True)
    createdTime = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['createdTime']

class ReviewRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=None)
    title = models.ForeignKey(RecipeDetails,on_delete=models.CASCADE)
    rating = models.FloatField()
    review = models.TextField(max_length=500, blank=True)
    created_review = models.DateTimeField(auto_now_add=True)
    updated_review = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review



