from rest_framework import serializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from for_test.models import Product, Lesson, Group
from .serializers import LessonSerializer
from .utils import distribute_user_to_groups
from for_test.serializers import ProductSerializer


class ProductLessonsView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise Http404("Продукт не существует")

        if not request.user.has_perm('view_product', product):
            return Response({'error': 'У вас нет доступа к этому продукту.'}, status=status.HTTP_403_FORBIDDEN)

        distribute_user_to_groups(product, request.user)
        lessons = Lesson.objects.filter(product_id=product_id)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)


class UserProductLessonsView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise Http404("Продукт не существует")

        if not request.user.has_perm('view_product', product):
            return Response({'error': 'У вас нет доступа к этому продукту.'}, status=status.HTTP_403_FORBIDDEN)

        distribute_user_to_groups(product, request.user)
        lessons = Lesson.objects.filter(product=product)
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)

class AvailableProductsView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
