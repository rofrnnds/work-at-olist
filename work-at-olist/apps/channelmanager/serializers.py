from rest_framework import serializers
from .models import Channel, Category


class RecursiveField(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ChannelSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='channels-api-detail')

    class Meta:
        model = Channel
        fields = ('name', 'id', 'url')


class CategorySerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='categories-api-detail')

    class Meta:
        model = Category
        fields = ('name', 'id', 'url')


class CategoryTreeSerializer(serializers.HyperlinkedModelSerializer):

    parent = CategorySerializer(many=False, read_only=True)
    children = RecursiveField(many=True, required=False)
    url = serializers.HyperlinkedIdentityField(
        view_name='categories-api-detail')

    class Meta:
        model = Category
        fields = ('name', 'id', 'url', 'children', 'parent',)
