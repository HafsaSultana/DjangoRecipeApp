from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import RecipeDetails
from django.contrib.auth.mixins import LoginRequiredMixin

class User_Login_View(LoginView):
    template_name = 'DjangoRecipeApp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('Recipe_List')

class Recipe_List(LoginRequiredMixin,ListView):
    model = RecipeDetails
    context_object_name = "Recipes"

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['Recipes'] = context['Recipes'].filter(user=self.request.user)
    #     return context



class Recipe_Details(DetailView):
    model = RecipeDetails
    context_object_name = "Recipe"
    template_name = 'DjangoRecipeApp/recipe_details.html'

class Recipe_Create(LoginRequiredMixin, CreateView):
    model = RecipeDetails
    fields = '__all__'
    success_url = reverse_lazy('Recipe_List')

class Recipe_Update(LoginRequiredMixin, UpdateView):
    model = RecipeDetails
    fields = '__all__'
    success_url = reverse_lazy('Recipe_List')



class Recipe_Delete(LoginRequiredMixin, DeleteView):
    model = RecipeDetails
    context_object_name = "Recipe"
    template_name = 'DjangoRecipeApp/recipe_delete.html'
    success_url = reverse_lazy('Recipe_List')

