from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet


from . import serializers
from .models import Category



class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def get_serializer_class(self):
        return serializers.CategoryListSerializer
