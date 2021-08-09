from rest_framework.serializers import ModelSerializer
from .models import *
from django.db.models import fields

class Todoserialize(ModelSerializer):
    class Meta:
        model = Todomodel
        fields = '__all__'
