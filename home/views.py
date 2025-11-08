from django.shortcuts import render
from .models import MenuCategory
from .serializers import MenuCategorySerializer
# Create your views here.
class MenuCategoryListView(ListAPIView):
    queryset=MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
