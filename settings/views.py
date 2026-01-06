from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Product, ContactMessage

def home(request):
    cat_filter = request.GET.get('cat')
    products = Product.objects.all()
    
    if cat_filter and cat_filter != 'All':
        products = products.filter(category=cat_filter)
        
    # Render index.html
    return render(request, 'index.html', {'products': products})

def about(request):
    # Render about.html
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message
        )
        return render(request, 'contact.html', {'success': True})
        
    # Render contact.html
    return render(request, 'contact.html')

from django.shortcuts import render, get_object_or_404
from .models import Product, ContactMessage

# ... home, about, contact functions ...

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # Ensure this line says 'details.html'
    return render(request, 'details.html', {'product': product})

def home(request):
    cat_filter = request.GET.get('cat')
    search_query = request.GET.get('q') # This reads the search box
    
    products = Product.objects.all()
    
    # Filter by Category if selected
    if cat_filter and cat_filter != 'All':
        products = products.filter(category=cat_filter)
        
    # Filter by Search if typed
    if search_query:
        products = products.filter(name__icontains=search_query)
        
    context = { 
        'products': products
    }
    return render(request, 'index.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Order

# ... existing views ...

def checkout(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        # Get user inputs (Shipping & Payment)
        payment_method = request.POST.get('payment_method')
        card_number = request.POST.get('card_number')
        card_expiry = request.POST.get('card_expiry')
        card_cvv = request.POST.get('card_cvv')
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        
        # Save to Database
        Order.objects.create(
            # CHANGED: Use the product object directly (Safer!)
            product_name = product.name, 
            price = product.price,
            
            # Use form data
            payment_method = payment_method,
            card_number = card_number,
            card_expiry = card_expiry,
            card_cvv = card_cvv,
            full_name = full_name,
            address = address,
            city = city,
            zip_code = zip_code
        )
        
        # Show Success Message
        return render(request, 'checkout.html', {'product': product, 'success': True})
        
    return render(request, 'checkout.html', {'product': product})