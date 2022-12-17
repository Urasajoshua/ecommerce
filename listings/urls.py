from django.urls import path
from . import views

app_name = "listings"
urlpatterns = [
    path("", views.ProductList, name="lists"),
    path("<slug:category_slug>", views.ProductList, name="product_list_by_category"),
    path("<slug:category_slug>/<slug:product_slug>/",views.product_detail,name="product_detail"),
]
