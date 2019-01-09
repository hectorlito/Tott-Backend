from rest_framework import serializers
from .models import Blog, FM


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
        )

        model = Blog


class FMSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'challenge',
            'writeup',
        )

        model = FM
