from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from .utils import generate_tags_from_description

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            description = product.description  # Assuming there's a description field
            generated_tags = generate_tags_from_description(description)
            
            # Save the tags to the product instance
            product.tags = generated_tags  # Assuming a field `tags` exists in your model
            product.save()
            return redirect('product_list')  # Redirect to the product list page
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})
