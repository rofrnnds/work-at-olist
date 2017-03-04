from rest_framework import viewsets
from apps.channelmanager.models import Channel, Category
from apps.channelmanager.serializers import ChannelListSerializer, \
    ChannelDetailSerializer, CategoryListSerializer, CategoryDetailSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ChannelViewSet(viewsets.ViewSet):

    """
    API endpoint that allows channels to be viewed

    list:
    Return all channels

    retrieve:
    Return a channel with all their categories and subcategories
    (flat representation)

    """

    def list(self, request):
        queryset = Channel.objects.all()
        serializer = ChannelListSerializer(queryset, many=True,
                                           context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        queryset = Channel.objects.all()
        channel = get_object_or_404(queryset, slug=slug)
        serializer = ChannelDetailSerializer(
            channel, context={'request': request})
        return Response(serializer.data)

    lookup_field = ('slug')


class CategoryViewSet(viewsets.ViewSet):

    """
    API endpoint that allows categories to be viewed

    list:
    Return all categories

    retrieve:
    Return a category with all their subcategories
    (hierarchical representation)

    """

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategoryListSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, slug=slug)
        serializer = CategoryDetailSerializer(
            category, context={'request': request})
        return Response(serializer.data)

    lookup_field = ('slug')
