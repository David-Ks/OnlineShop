from django.urls import path

from .views import *

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("products/", ProductList.as_view(), name="products"),
    path("products/<int:pk>/", ProductDetail.as_view(), name="prdouctDetail"),
    path("chackout/", ChackOutView.as_view(), name="chackout"),
]
