from rest_framework import serializers
from .models import Homework


class HomeworkSerializers(serializers.ModelSerializer):

    class Meta:
        model = Homework
        # exclude = ['name']
        fields = '__all__'
        # fields = ['name']
