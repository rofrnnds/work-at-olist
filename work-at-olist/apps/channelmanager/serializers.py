from rest_framework import serializers
from .models import Channel, Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='categories-api-detail')

    class Meta:
        model = Category
        fields = ('url', 'id', 'name')


class ChannelSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='channels-api-detail')

    class Meta:
        model = Channel
        fields = ('url', 'id', 'name')


class CategoryTreeSerializer(serializers.HyperlinkedModelSerializer):
    parent = CategorySerializer(many=False, read_only=True)
    children = CategorySerializer(many=True, read_only=True)

    url = serializers.HyperlinkedIdentityField(
        view_name='categories-api-detail')

    class Meta:
        model = Category
        fields = ('url', 'parent', 'id', 'name', 'children')
