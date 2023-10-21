from django.shortcuts import get_object_or_404, render
from .models import Listing
from django.core.paginator import Paginator, PageNotAnInteger
from .choices import price_choices, bedroom_choices, state_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    
    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    
    context = {
        "listings": paged_listings,
    }
    return render(request, "listings/listings.html", context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        "listing": listing
    }
    return render(request, "listings/listing.html", context)

def search(request):
    query_listing = Listing.objects.order_by('-list_date')

    # Keywords
    if 'keywords' in request.GET:
        if keywords := request.GET['keywords']:
            query_listing = query_listing.filter(description__icontains = keywords)
    # cities
    if 'city' in request.GET:
        if city := request.GET['city']:
            query_listing = query_listing.filter(city__iexact= city)
        
    # State
    if 'state' in request.GET:
        if state := request.GET['state']:
            query_listing = query_listing.filter(state__iexact= state)
    
    # bedrooms
    if 'bedrooms' in request.GET:
        if bedrooms := request.GET['bedrooms']:
            query_listing = query_listing.filter(bedrooms__lte= bedrooms)
        
    # price
    if 'price' in request.GET:
        if price := request.GET['price']:
            query_listing = query_listing.filter(price__lte= price)

    context = {
        "bedroom_choices": bedroom_choices,
        "state_choices": state_choices,
        "price_choices": price_choices,
        "listings" : query_listing,
        "values": request.GET,
    }
    return render(request, "listings/search.html", context)