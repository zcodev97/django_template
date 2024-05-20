from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.conf import settings
from .models import (Container)

from core.serializers import CustomUserSerializer


class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = ('id', 'name', 'total_dinar',
                  'total_dollar', 'created_at', 'created_by')
