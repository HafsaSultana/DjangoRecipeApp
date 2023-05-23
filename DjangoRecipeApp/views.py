from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotAllowed
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView, FormView

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import RecipeDetails,Category_Tag, ReviewRating
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin
#register
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from django import forms
from django.db.models import Subquery
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from taggit.models import Tag
from django.core.paginator import Paginator

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

class Recipe_List(LoginRequiredMixin, ListView):
    model = RecipeDetails
    context_object_name = "Recipes"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        search_input = self.request.GET.get('search-area') or ''
        search_category = self.request.GET.get('search-category') or ''
        search_tag = self.request.GET.get('search-tag') or ''

        if search_input:
            queryset = queryset.filter(title__icontains=search_input)

        if search_category:
            queryset = queryset.filter(category__name=search_category)

        if search_tag:
            queryset = queryset.filter(tags__name=search_tag)

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category_Tag.objects.all()
        context['tags'] = Tag.objects.all()
        context['search_input'] = self.request.GET.get('search-area') or ''
        context['search_category'] = self.request.GET.get('search-category') or ''
        context['search_tag'] = self.request.GET.get('search-tag') or ''
        return context


class Recipe_Details( DetailView):
    model = RecipeDetails
    context_object_name = "Recipe"
    #categories = Category_Tag.objects.all()
    template_name = 'DjangoRecipeApp/recipe_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context["now"] = timezone.now()
        recipe = self.object
        context['categories'] = self.object.category.all()  # Access the categories related to the recipe
        context['comment'] = recipe.reviewrating_set.all()  # Ratings related to the recipe
        return context

    def post(self, request, *args, **kwargs):
        # Get the rating and comment values from the form
        recipe = self.get_object()
        rating_value = float(request.POST.get('rating'))
        comment = request.POST.get('review')
        # Get the recipe object based on the recipe_id
        # Create a new ReviewRating object
        review = ReviewRating(user=request.user, title=recipe, rating=rating_value, review=comment)
        # Save the ReviewRating object to the database
        review.save()
        # Show a success message
        messages.success(request, 'Rating and review posted successfully.')
        # Redirect to the recipe details page
        return redirect('Recipe_Details',pk=recipe.pk)


class Recipe_Create(LoginRequiredMixin, CreateView):
    model = RecipeDetails
    # fields = '__all__'
    fields = ['title','category','tags','description','ingredientList','introduction','image','video',]
    success_url = reverse_lazy('Recipe_List')

    def form_valid(self, form):
        form.instance.user = self.request.user

        # Handle uploaded image
        image_file = self.request.FILES.get('image')
        if image_file:
            form.instance.image = image_file

        # Handle uploaded video
        video_file = self.request.FILES.get('video')
        if video_file:
            form.instance.video = video_file

        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class Recipe_Update(LoginRequiredMixin, UpdateView):
    model = RecipeDetails
    #fields = '__all__'
    fields = ['title', 'category','tags','description', 'ingredientList', 'introduction', 'image', 'video',]
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


class RecipeRatingView(View):
    def post(self, request, recipe_id):
        # Get the rating and comment values from the form
        rating_value = float(request.POST.get('rating'))
        comment = request.POST.get('review')
        # Get the recipe object based on the recipe_id
        recipe = RecipeDetails.objects.get(id=recipe_id)
        # Create a new ReviewRating object
        review = ReviewRating(user=request.user, title=recipe, rating=rating_value, review=comment)
        # Save the ReviewRating object to the database
        review.save()
        # Show a success message
        messages.success(request, 'Rating and review posted successfully.')
        # Redirect to the recipe details page
        return redirect('recipe_details', recipe_id=recipe_id)

class Recipe_Comment( DetailView):
    model = ReviewRating
    context_object_name = "Comment"
    template_name = 'DjangoRecipeApp/recipe_comment.html'

