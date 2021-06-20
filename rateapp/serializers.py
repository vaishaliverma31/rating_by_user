from rest_framework import serializers
from.models import *

class applicationsserializers(serializers.ModelSerializer):
    class Meta:
        model=application
        fields='__all__'

class user_defineserializer(serializers.ModelSerializer):
    class Meta:
        model=user_define
        fields='__all__'

        from django.contrib.auth.models import User
class userseializer(serializers.ModelSerializer):
        class Meta:
          model = User
          fields = ['username', 'password']