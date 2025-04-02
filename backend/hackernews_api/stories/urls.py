from django.urls import path
from . import views

urlpatterns = [
    path('top-stories/', views.get_top_news_stories, name='top_news_stories'),
]