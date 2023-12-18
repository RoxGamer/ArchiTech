from django.contrib import admin
from django.urls import path, include
from Capstone12 import views
# from Capstone12.views import index

urlpatterns = [
    path('', views.index, name='color_image'),
    path('get-started/', views.get_started, name='get_started'),
    path('', views.go_home, name='go_home'),
    # path('get-started', views.color_image, name='color_image'),
    path('regenerate/', views.regenerate_image, name='regenerate_image'),
    path('clear/', views.clear_image, name='clear_image'),
    # path('regenerate/', views.regenerate_image, name='regenerate_image'),
    
]
