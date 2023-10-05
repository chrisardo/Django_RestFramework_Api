from rest_framework import serializers
from .models import Programmer


class ProgrammerSerializr(serializers.ModelSerializer):
    class Meta:
        model = Programmer
        # fields = ['fullname', 'nickname', 'age', 'is_active']
        fields = '__all__'
