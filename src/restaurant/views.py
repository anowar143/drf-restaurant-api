from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.parsers import FileUploadParser
from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly


class RestaurantCreateView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantUpdateView(RetrieveUpdateAPIView):
    permission_classes = (AllowAny,)
    queryset = Restaurant.objects.filter()
    serializer_class = RestaurantSerializer
    lookup_field = 'id'
