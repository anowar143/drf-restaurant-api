from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from order.models import Cart, Order, Discount
from order.serializers import CartSerializer, OrderSerializer, DiscountSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

class CartCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartUpdateView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Cart.objects.filter()
    serializer_class = CartSerializer
    lookup_field = 'id'


class OrderCreateView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.filter()
    serializer_class = OrderSerializer
    lookup_field = 'id'


class DiscountCreateView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class DiscountUpdateView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Discount.objects.filter()
    serializer_class = DiscountSerializer
    lookup_field = 'id'
