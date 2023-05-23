from django.contrib import admin
from .models import RecipeDetails
from .models import ReviewRating

from .models import Category_Tag
# Register your models here.

admin.site.register(RecipeDetails)
admin.site.register(ReviewRating)
admin.site.register(Category_Tag)