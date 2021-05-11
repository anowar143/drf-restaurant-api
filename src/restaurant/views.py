from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.parsers import FileUploadParser
from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly


class RestaurantCreateView(ListCreateAPIView):
    parser_class = (FileUploadParser,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantUpdateView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Restaurant.objects.filter()
    serializer_class = RestaurantSerializer
    lookup_field = 'id'
