from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.parsers import FileUploadParser
from food.models import Food, FoodCategory
from food.serializers import FoodSerializer, FoodCategorySerializer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly


class FoodCategoryCreateView(ListCreateAPIView):
    parser_class = (FileUploadParser,)
    permission_classes = (AllowAny, )
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer

class FoodCategoryUpdateView(RetrieveUpdateAPIView):
    permission_classes = (AllowAny, )
    queryset = FoodCategory.objects.filter()
    serializer_class = FoodCategorySerializer
    lookup_field = 'id'


class FoodCreateView(ListCreateAPIView):
    parser_class = (FileUploadParser,)
    permission_classes = (AllowAny, )
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class FoodUpdateView(RetrieveUpdateAPIView):
    permission_classes = (AllowAny, )
    queryset = Food.objects.filter()
    serializer_class = FoodSerializer
    lookup_field = 'id'

    def perform_update(self, serializer):
        serializer.save()
