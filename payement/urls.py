
from django.urls import path
from . import views

app_name="payement"
urlpatterns = [
    path('done/',views.payement_done,name='done'),
    path('canceled/',views.payement_canceled,name='canceled'),


]