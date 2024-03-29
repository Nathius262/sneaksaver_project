from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from operator import attrgetter
from sneaksaver.models import Product, CleanService, Message
from .models import CleanServiceSearch, ProductSearch, TopSearch, FrequentlyAskedQuestion

# Create your views here.
def generic_view(request):
    context = {
        'product_search': ProductSearch.objects.all()[:3],
        'service_search': CleanServiceSearch.objects.all(),
    }
    return context

# SEARCH POST FUNCTION
def get_product_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        product = Product.objects.all().filter(
            Q(name__icontains=q) |
            Q(price__icontains=q) |
            Q(tag__name__icontains=q) |
            Q(description__icontains=q)
        ).distinct()
        for products in product:
            queryset.append(products)
    return list(set(queryset))

def get_clean_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        service = CleanService.objects.all().filter(
            Q(service_name__icontains=q) |
            Q(service_price__icontains=q)
        ).distinct()
        for services in service:
            queryset.append(services)
    return list(set(queryset))

def get_faq_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        service = FrequentlyAskedQuestion.objects.all().filter(
            Q(title__icontains=q) |
            Q(content__icontains=q)
        ).distinct()
        for services in service:
            queryset.append(services)
    return list(set(queryset))

def search_view(request):
    context = {}

    query = ""
    if request.GET:
        query = request.GET.get('q')
        context['query'] = str(query)
        
        top_search, created = TopSearch.objects.get_or_create(name=query)
        top_search.search_count += 1
        top_search.save()
        
        product = sorted(get_product_queryset(query), key=attrgetter('date'), reverse=True)

        # Pagination
        POSTS_PER_PAGE = 9
        page = request.GET.get('page', 1)
        post_paginator = Paginator(product, POSTS_PER_PAGE)

        try:
            product = post_paginator.page(page)
        except PageNotAnInteger:
            product = post_paginator.page(POSTS_PER_PAGE)
        except EmptyPage:
            product = post_paginator.page(post_paginator.num_pages)

        service = get_clean_queryset(query)
        faq = get_faq_queryset(query)
        
        #search result couter
        if product:
            for items in product:
                search_result, _ = ProductSearch.objects.get_or_create(product=items)
                search_result.search_count += 1
                search_result.save()
        if service:
            for items in service:
                search_result, created = CleanServiceSearch.objects.get_or_create(service=items)
                search_result.search_count += 1
                search_result.save()

        context = {
            'all_product': product,
            'service':service,
            'faq_content':faq,
            'query': query,
            'top_search': TopSearch.objects.all()[:6]
        }
    return render(request, 'data_analysis/search.html', context)


def faq_views(request):
    message = Message.objects.all().filter(user=request.user.user_profile)
    context = {
        'faq':True,
        'faq_content':FrequentlyAskedQuestion.objects.all(),
        'message_field':True,
        'message':message
    }
    return render(request, "data_analysis/faqs.html", context)