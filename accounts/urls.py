from django.urls import path
# from .views import signup
from . import views

urlpatterns = [
   
    path('signup',views.signup,name="signup"),
   
    
]