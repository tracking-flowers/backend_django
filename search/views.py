from django. shortcuts import render
from rest_framework import generics, filters
from search.models import Food
from search.serializer import FoodSerializer

class FoodAPIView(generics.ListCreateAPIView):
    search_fields = ['name', 'price']
    filter_backends = (filters.SearchFilter,)
    queryset = Food.objects.all()
    serializer_class = FoodSerializer