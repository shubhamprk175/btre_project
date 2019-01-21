from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from .models import Listing
from realtors.models import Realtor
from .choices import bedroom_choice, price_choice, state_choice
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 6)

    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        "listings": paged_listings
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    query_listings = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_listings = query_listings.filter(description__icontains=keywords)
    
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            query_listings = query_listings.filter(city__iexact=city)
    
    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            query_listings = query_listings.filter(state__iexact=state)
    
    # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            query_listings = query_listings.filter(bedrooms__lte=bedrooms)
        
    # Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_listings = query_listings.filter(price__lte=price)
    

    context = {
        'bedroom_choice': bedroom_choice,
        'price_choice': price_choice,
        'state_choice': state_choice,
        'listings': query_listings,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)
