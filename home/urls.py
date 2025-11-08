from django.urls import path
from .views import *

urlpatterns = [
    path('categories/',MenuCategoryListView(), name='manu-categories'),
]