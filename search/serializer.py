from rest_framework import serializers
from search.models import Food

# class OuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ouestion
#         fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'