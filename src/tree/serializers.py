from rest_framework import serializers

from tree.models import Node, Tag


class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class NodeTreeSerializer(serializers.ModelSerializer):
    children = RecursiveField(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Node
        fields = [
            'id',
            'parent',
            'value',
            'tags',
            'children',
        ]


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'
