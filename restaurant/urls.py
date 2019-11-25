
from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
   path('', views.index, name='index'),
   path('search/', views.search, name='search'),
   path('<int:restaurant_pk>/', views.detail, name='detail'),
   path('chatbot_how_to_use/', views.chatbot_how_to_use, name='chatbot_how_to_use'),
]
