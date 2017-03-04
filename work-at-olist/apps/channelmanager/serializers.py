from rest_framework import serializers
from .models import Channel, Category


class RecursiveField(serializers.Serializer):

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CategoryListSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name='categories-api-detail', lookup_field='slug')

    class Meta:
        model = Category
        fields = ('name', 'url')


class CategoryDetailSerializer(serializers.HyperlinkedModelSerializer):

    parent = CategoryListSerializer(many=False, read_only=True)
    children = RecursiveField(many=True, required=False)
    url = serializers.HyperlinkedIdentityField(
        view_name='categories-api-detail', lookup_field='slug')

    class Meta:
        model = Category
        fields = ('name', 'url', 'children', 'parent',)


class ChannelListSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='channels-api-detail',
                                               lookup_field='slug')

    class Meta:
        model = Channel
        fields = ('name', 'url')


class ChannelDetailSerializer(serializers.HyperlinkedModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='channels-api-detail',
                                               lookup_field='slug')

    categories = CategoryListSerializer(many=True, read_only=True)

    class Meta:
        model = Channel
        fields = ('name', 'url', 'categories')
