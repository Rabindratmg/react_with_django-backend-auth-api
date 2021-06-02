from .models import Login
from rest_framework import serializers
from .models import Login 


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'