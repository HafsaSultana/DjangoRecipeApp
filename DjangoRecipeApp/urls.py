from django.urls import path
from .views import Recipe_List,Recipe_Details,Recipe_Create,Recipe_Update,Recipe_Delete,User_Login_View
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',User_Login_View.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(next_page='user-login'), name='user-logout'),

    path('', Recipe_List.as_view(), name='Recipe_List'),
    path('recipe/<int:pk>/', Recipe_Details.as_view(), name='Recipe_Details'),
    path('recipe-create/', Recipe_Create.as_view(), name='recipe-create'),
    path('recipe-update/<int:pk>/', Recipe_Update.as_view(), name='recipe-update'),
    path('recipe-delete/<int:pk>/', Recipe_Delete.as_view(), name='recipe-delete'),

]