# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from rest_framework import viewsets, generics

from tree.models import Node, Tag
from tree.serializers import NodeSerializer, NodeTreeSerializer, TagSerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class NodeTreeList(generics.ListAPIView):
    serializer_class = NodeTreeSerializer

    def get_queryset(self):
        return Node.objects.filter(parent__isnull=True)
