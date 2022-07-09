from rest_framework import generics

from .serilaizers import *


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDetailView(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ManufacturerListView(generics.ListAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class ManufacturerDetailView(generics.RetrieveAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetailView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class CommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
