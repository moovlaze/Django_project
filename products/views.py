from django.shortcuts import render

from products.models import ProductCategory, Product


def index(request):
    context = {"title": "test title"}
    return render(request, "products/index.html", context=context)


def products(request):
    context = {
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all()
    }

    return render(request, "products/products.html", context=context)
