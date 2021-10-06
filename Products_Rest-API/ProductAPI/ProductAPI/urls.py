"""ProductAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:productName>', views.show_product_by_name,name="show_product_by_name"),
    path('products/', views.show_products,name="show_products"),
    path('products/<int:productID>', views.products_by_id,name="products_by_id"),
    path('products/<str:productName>', views.show_product_by_name,name="products_by_name"),
    path('category/', views.display_category,name="display_category"),
    path('category/add', views.add_category,name="add_category"),
    path('category/<int:categoryID>', views.category_by_id,name="category_by_id"),
    path('category/<str:categoryname>', views.category_by_name,name="category_by_name"),
    path('product/category/<int:categoryID>', views.product_by_category,name="product_by_category"),
    path('product/category/<str:categoryname>', views.product_by_categoryName,name="product_by_categoryName"),
    path('product/update/<int:productID>', views.update_product_by_id,name="update_product_by_id"),
]
