from django.urls import path

from order.views import CartCreateView, CartUpdateView, OrderCreateView, OrderUpdateView, DiscountCreateView, DiscountUpdateView

urlpatterns = [
    path('cart/', CartCreateView.as_view(),),
    path('cart/<int:id>/', CartUpdateView.as_view(),),
    path('order/', OrderCreateView.as_view(),),
    path('order/<int:id>/', OrderUpdateView.as_view(),),
    path('discount/', DiscountCreateView.as_view(), ),
    path('discount/<int:id>/', DiscountUpdateView.as_view(), ),

]
