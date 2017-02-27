from rest_framework import serializers
from .models import Channel, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Channel
        fields = ('id', 'name')


class CategoryTreeSerializer(serializers.ModelSerializer):
    parent = CategorySerializer(many=False, read_only=True)
    children = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('parent', 'id', 'name', 'children')
