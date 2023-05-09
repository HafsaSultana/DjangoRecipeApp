from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import RecipeDetails,Category_Tag

from django.contrib.auth.mixins import LoginRequiredMixin
#register
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django import forms
from django.db.models import Subquery


class User_Login_View(LoginView):
    template_name = 'DjangoRecipeApp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('Recipe_List')

class User_Register_Page(FormView):
    template_name = 'DjangoRecipeApp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('Recipe_List')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(User_Register_Page,self).form_valid(form)


class Recipe_Category_Tag(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Category_Tag.objects.all())

    class Meta:
        model = RecipeDetails
        fields = '__all__'


class Recipe_List(LoginRequiredMixin,ListView):
    model = RecipeDetails
    context_object_name = "Recipes"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['Recipes'] = context['Recipes'].filter(user=self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input :
            context['Recipes'] = context['Recipes'].filter(title__icontains = search_input).all()
            # context['Recipes'] = context['Recipes'].filter(category__name=search_input)

            context['search_input'] = search_input

        return context



class Recipe_Details(DetailView):
    model = RecipeDetails
    context_object_name = "Recipe"
    template_name = 'DjangoRecipeApp/recipe_details.html'

class Recipe_Create(LoginRequiredMixin, CreateView):
    model = RecipeDetails
    fields = '__all__'
    #fields = ['title','category','description','ingredientList','introduction','image','video','createdTime']
    success_url = reverse_lazy('Recipe_List')

    # def form_valid(self, form):
    #     form.instance.use = self.request.user
    #     return super(Recipe_Create,self).form_valid(form)

class Recipe_Update(LoginRequiredMixin, UpdateView):
    model = RecipeDetails
    fields = '__all__'
    #fields = ['title', 'category', 'description', 'ingredientList', 'introduction', 'image', 'video', 'createdTime']
    success_url = reverse_lazy('Recipe_List')



class Recipe_Delete(LoginRequiredMixin, DeleteView):
    model = RecipeDetails
    context_object_name = "Recipe"
    template_name = 'DjangoRecipeApp/recipe_delete.html'
    success_url = reverse_lazy('Recipe_List')

class Recipe_Comment(DetailView):
    model = RecipeDetails
    context_object_name = "Recipe"
    template_name = 'DjangoRecipeApp/recipe_comment.html'
    success_url = reverse_lazy('Recipe_List')

