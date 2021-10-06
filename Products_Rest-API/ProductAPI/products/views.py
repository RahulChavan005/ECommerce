from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# Create your views here.

def show_category(request,hierarchy= None):
    category_slug = hierarchy.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [ x.slug for x in category_queryset ]
    parent = None
    for slug in category_slug:
        if slug in all_slugs:
            parent = get_object_or_404(Category,slug=slug,parent=parent)
        else:
            instance = get_object_or_404(Product, slug=slug)
            breadcrumbs_link = instance.get_cat_list()
            category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
            breadcrumbs = zip(breadcrumbs_link, category_name)
            return render(request, "products/postDetail.html", {'instance':instance,'breadcrumbs':breadcrumbs})

    return render(request,"products/categories.html",{'product_set':parent.product_set.all(),'sub_categories':parent.children.all()})

@api_view(['GET'])
def show_products(request):
    # api = {'sample json response'}
    # return Response(api)

    products = Product.objects.all()
    serializer = productSerializer(products, many= True)

    return Response(serializer.data)

@api_view(['GET'])
def display_category(request):
    # api = {'sample json response'}
    # return Response(api)

    categories = Category.objects.all()
    serializer = categorySerialzer(categories, many= True)

    return Response(serializer.data)

@api_view(['GET'])
def category_by_name_obsolete(request,categoryname):
    # categories = Category.objects.all()
    # serializer = categorySerialzer(categories, many= True)
    category_queryset = list(Category.objects.all())
    all_names = [ x.name for x in category_queryset ]

    print(all_names)
    print(categoryname)
    parent = None
    #for slug in category_slug:
    if categoryname in all_names:
        parent = get_object_or_404(Category,name=categoryname,parent=parent)
        print(parent)
    # else:
    #     instance = get_object_or_404(Product, name=categoryname)
    #     breadcrumbs_link = instance.get_cat_list()
    #     category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
    #     breadcrumbs = zip(breadcrumbs_link, category_name)
    #     return HttpResponse(breadcrumbs)
        #return render(request, "products/postDetail.html", {'instance':instance,'breadcrumbs':breadcrumbs})

    sub_categories = parent.children.all()

    print(sub_categories)
    serializer = categorySerialzer(sub_categories, many= True)

    return Response(serializer.data)
    #eturn render(request,"products/categories.html",{'product_set':parent.product_set.all(),'sub_categories':parent.children.all()})

@api_view(['GET'])
def category_by_name(request,categoryname):
    categories = Category.objects.filter(name=categoryname)
    serializer = categorySerialzer(categories, many= True)

    return Response(serializer.data)

@api_view(['GET'])
def category_by_id(request,categoryID):
    categories = Category.objects.filter(id=categoryID)
    serializer = categorySerialzer(categories, many= True)

    return Response(serializer.data)

@api_view(['POST'])
def add_category(request):
    serializer = categorySerialzer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def product_by_category(request,categoryID):
    products = Product.objects.filter(category__id=categoryID)
    
    serializer = productSerializer(products, many= True)

    return Response(serializer.data)

@api_view(['GET'])
def product_by_categoryName(request,categoryname):
    products = Product.objects.filter(category__name=categoryname)
    
    serializer = productSerializer(products, many= True)

    return Response(serializer.data)

@api_view(['GET'])
def show_product_by_name(request,productName):

    # import pdb

    # pdb.set_trace()
    products = Product.objects.filter(productname = productName)

    serializer = productSerializer(products,many= True)

    return Response(serializer.data)

@api_view(['POST'])
def update_product_by_id(request,productID):
    product = Product.objects.get(id=productID)
    serializer = productSerializer(instance = product, data=request.data)

    if(serializer.is_valid()):
        serializer.save()

    return Response(serializer.data)

@api_view(['GET'])
def products_by_id(request,productID):
    products = Product.objects.get(id = productID)
    serializer = productSerializer(products)

    return Response(serializer.data)