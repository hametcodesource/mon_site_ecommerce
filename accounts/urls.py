from .forms import LoginForm
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name="accounts"
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name="accounts/login.html",redirect_authenticated_user=True,authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="accounts/logout.html",next_page="shop:product_list"),name='logout'),


]