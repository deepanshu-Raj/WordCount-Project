from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'home'),
    path('count/' , views.Count , name = 'count'),
    path('aboutus/', views.AboutUs ,name = 'about'),
    path('subscribe/', views.Subscribe ,name = 'subscribe')
]
