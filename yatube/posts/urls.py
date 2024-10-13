from . import views
from django.urls import path
urlpatterns = [
    path('', views.index),
    path('IceCream', views.index2),
    path('IceCream/<id>', views.index3),
    path('<id>', views.index4),
]