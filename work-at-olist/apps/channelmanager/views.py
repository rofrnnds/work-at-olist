from rest_framework import viewsets
from apps.channelmanager.models import Channel, Category
from apps.channelmanager.serializers import ChannelSerializer, \
    CategorySerializer, CategoryTreeSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class ChannelViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class CategoryViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        category = get_object_or_404(queryset, pk=pk)
        serializer = CategoryTreeSerializer(category)
        return Response(serializer.data)
