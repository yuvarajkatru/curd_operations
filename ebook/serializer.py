from rest_framework import serializers
from .models import ebook

class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = ebook
        fields = ['id','Title','Author','Genre','Review','Favorite']
