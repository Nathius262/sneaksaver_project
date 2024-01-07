from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, "index.html", {"loc":True})

def product_view(request):
    return render(request, "sneaksaver/product_list.html")

def product_detail_view(request):
    return render(request, "sneaksaver/product_detail.html")

def pricing_view(request):
    return render(request, "sneaksaver/pricing.html")

def booking_view(request):
    return render(request, "sneaksaver/booking.html")