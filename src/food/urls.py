from django.urls import path

from food.views import FoodCreateView, FoodUpdateView, FoodCategoryCreateView, FoodCategoryUpdateView

urlpatterns = [
    path('food/', FoodCreateView.as_view(),),
    path('food/<int:id>/', FoodUpdateView.as_view(),),
    path('category/', FoodCategoryCreateView.as_view(),),
    path('category/<int:id>/', FoodCategoryUpdateView.as_view(),),

]
