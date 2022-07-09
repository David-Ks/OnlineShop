from django.urls import path

from .views import *

urlpatterns = [
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),

    path('manufacturer/', ManufacturerListView.as_view()),
    path('manufacturer/<int:pk>/', ManufacturerDetailView.as_view()),

    path('product/', ProductListView.as_view()),
    path('product/<int:pk>/', ProductDetailView.as_view()),

    path('comments/', CommentListView.as_view())
]