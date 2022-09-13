from django.urls import path


from .views import *


# app_name = "ecommapp
urlpatterns = [
    path("index", index, name="index"),
    # path("", HomeView.as_view(), name="home")    
]
