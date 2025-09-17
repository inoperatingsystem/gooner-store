from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product

# Create your views here.
def show_main(request):
    product_list = Product.objects.all()

    context = {
        'app_name' : 'Gooner Store',
        'name' : 'Julius Albert Wirayuda',
        'class' : 'PBP F',
        'product_list': product_list,
    }

    return render(request, "main.html", context)

def add_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "add_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)