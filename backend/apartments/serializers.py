from rest_framework.serializers import ModelSerializer

from .models import Apartment

class ApartmentSerializer(ModelSerializer):
    class Meta:
        model = Apartment
        fields = ['id', 'title', 'price']