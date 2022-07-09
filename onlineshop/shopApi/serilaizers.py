from rest_framework import serializers

from shop.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['image']


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        exclude = ['logo']


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)
    manufacturer = serializers.SlugRelatedField(slug_field='title', read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Product
        exclude = ['image']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
