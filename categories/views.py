from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Category
from rest_framework.response import Response
from .serializers import CategorySerializer


# Create your views here
class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


"""class Categories(APIView):

    def get(self, request):
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(CategorySerializer(new_category).data)
        else:
            return Response(serializer.errors)


class CategoryDetail(APIView):

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise NotFound("Category does not exist")

    def get(self, request, pk):
        category_1 = self.get_object(pk)
        serializer = CategorySerializer(category_1)
        return Response(serializer.data)

    def put(self, request, pk):
        category_1 = self.get_object(pk)
        serializer = CategorySerializer(
            category_1,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            update_category = serializer.save()
            return Response(CategorySerializer(update_category).data)
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        category_1 = self.get_object(pk)
        category_1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""
