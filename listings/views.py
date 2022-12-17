from django.shortcuts import render ,get_object_or_404
from .models import Product ,Category


def ProductList(request ,category_slug=None):
    requested_category=None
    products=Product.objects.all()
    categories=Category.objects.all()

    if category_slug:
        requested_category=get_object_or_404(Category,slug=category_slug)
        products=Product.objects.filter(category=requested_category)

    context={
        'products':products,
        'categories':categories,
        'requested_category':requested_category
    }

    return render(request,'listings/list.html',context)


def product_detail(request, category_slug, product_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product,category_id = category.id,slug=product_slug)
    return render(request,'listings/detail.html',{'product': product,'category':category})