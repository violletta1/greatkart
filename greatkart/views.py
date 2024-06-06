from django.shortcuts import render

from store.models import Product, ReviewRating

def home(request):
    products = Product.objects.filter(is_available=True).order_by('created_date')
    reviews = []  # Initialize as empty list
    
    for product in products:
        # Get the reviews and append them to the list
        product_reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
        reviews.extend(product_reviews)
        
    context = {
        'products': products,
        'reviews': reviews
    }
    
    return render(request, 'home.html', context)