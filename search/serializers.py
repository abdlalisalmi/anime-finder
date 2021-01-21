from rest_framework import serializers
from .models import UploadImage

class UploadImageSerializer(serializers.Serializer):
    class Meta:
        model = UploadImage
        fields = ['image']