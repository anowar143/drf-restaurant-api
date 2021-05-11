from django.urls import path


from restaurant.views import RestaurantCreateView, RestaurantUpdateView

urlpatterns = [
    path('restaurant/', RestaurantCreateView.as_view(),),
    path('restaurant/<int:id>/', RestaurantUpdateView.as_view(),),
]
