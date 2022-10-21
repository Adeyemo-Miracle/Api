from rest_framework import serializers
from app.models import App

class appSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'