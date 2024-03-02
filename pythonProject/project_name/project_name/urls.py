from django.urls import path
from for_test.views import ProductLessonsView, AvailableProductsView, UserProductLessonsView

urlpatterns = [
    path('products/<int:product_id>/lessons/', ProductLessonsView.as_view(), name='product_lessons'),
    path('available_products/', AvailableProductsView.as_view(), name='available_products'),
    path('user_products/<int:product_id>/lessons/', UserProductLessonsView.as_view(), name='user_product_lessons'),
]
