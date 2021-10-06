from django.core.files.base import ContentFile
from shopping.models import Customer, Product
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from . import forms
# Create your views here.


def index(request):
    return HttpResponse("Homepage")


def home(request):
    products = Product.objects.all()
    context = {
        "products": products
    }

    return render(request, "shopping/home.html", context=context)


def placeOrder(request, custID):
    customer = Customer.objects.get(id=custID)
    form = forms.createOrderForm(instance=customer)
    if(request.method == "POST"):
        form = forms.createOrderForm(request.POST, instance=customer)
        if(form.is_valid()):
            form.save()
            return redirect("/")

    context = {"form": form}

    return render(request, "shopping/placeOrder.html", context=context)


def addProduct(request):
    # import pdb
    # pdb.set_trace()
    form = forms.createproductform()
    if(request.method == "POST"):
        form = forms.createproductform(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('/')

    context = {"form": form}

    return render(request, "shopping/addProduct.html", context)


def registerPage(request):
    # import pdb
    # pdb.set_trace()
    if request.user.is_authenticated:
        return redirect("home")
    else:
        form = forms.createuserform()
        customerform = forms.createcustomerform()
        if(request.method == "POST"):
            form = forms.createuserform(request.POST)
            customerform = forms.createcustomerform(request.POST)
            if(form.is_valid() and customerform.is_valid()):
                user = form.save()
                customer = customerform.save(commit=False)
                customer.user = user
                customer.save()
                return redirect("login")

        context = {"form": form, "customerform": customerform}
        return render(request, "shopping/registerPage.html", context= context)
        # return HttpResponse("This is Register Page")

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method == "POST":
           username = request.POST.get('username')
           password = request.POST.get('password')
           user = authenticate(request, username=username, password=password)
           if user is not None:
               login(request, user)
               return redirect('/')
       context = {}
       return render(request, 'shopping/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('/')
