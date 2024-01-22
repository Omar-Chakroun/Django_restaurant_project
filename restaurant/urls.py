#define URL route for index() view
from django.urls import path
from . import views
from .views import SingleMenuItemView,MenuItemView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', views.index, name='index'),
    path('menu/items/', views.MenuItemView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
   ]
