from django.urls import path
 
from . import views
 
urlpatterns = [ 
     path('add_model/', views.add_model, name='add_model'),
]