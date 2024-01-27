from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, BookingForm
from .models import CleanService, Message
from .utils import send_email_view
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from operator import attrgetter
from .models import Product, ShoeModel
from django.http import JsonResponse
from hitcount.views import HitCountDetailView
from django.db.models import Count


# Create your views here.


def index_view(request):
    context = {
        'product':Product.objects.all()[:6],
        'popular_posts': Product.objects.order_by('-hit_count_generic__hits')[:6],
        "loc":True
    }
    return render(request, "index.html", context)

def product_view(request):
    context = {}
    POSTS_PER_PAGE = 12
    all_product = sorted(Product.objects.all(), key=attrgetter('name'), reverse=True)
    context['all_product'] = all_product

    # Pagination
    page = request.GET.get('page', 1)
    all_post_paginator = Paginator(all_product, POSTS_PER_PAGE)

    try:
        all_product = all_post_paginator.page(page)
    except PageNotAnInteger:
        all_product = all_post_paginator.page(POSTS_PER_PAGE)
    except EmptyPage:
        all_product = all_post_paginator.page(all_post_paginator.num_pages)
    context['all_product'] = all_product

    return render(request, "sneaksaver/product_list.html", context)


class DetailPostView(HitCountDetailView):
    model = Product
    template_name = 'sneaksaver/product_detail.html'
    context_object_name = 'product'
    slug_field = 'slug'
    count_hit = True

    def get_queryset(self):
        products = Product.objects.all().filter(slug=self.kwargs['slug'])
        return products

    def get_context_data(self, **kwargs):
        context = super(DetailPostView, self).get_context_data(**kwargs)
        product = self.get_queryset()
        product = product.first()

        tag = ShoeModel.objects.all()
        related_post = Product.objects.filter(tag__in=tag).exclude(slug=self.kwargs['slug'])
        related_post = related_post.annotate(tag_count=Count('tag')).order_by('-tag_count', '-date')

        context.update({
            'popular_posts': Product.objects.order_by('-hit_count_generic__hits')[:3],
            'related_post':related_post[:1],
            'tag': tag,
        })
        return context


def pricing_view(request):
    context = {
        "price_standard":CleanService.objects.get_or_create(service_name__icontains="standard"),
        "price_deep":CleanService.objects.get_or_create(service_name__icontains="deep"),
        "price_premium":CleanService.objects.get_or_create(service_name__icontains="premium"),
    }
    return render(request, "sneaksaver/pricing.html", context)

def booking_view(request):
    context = {}
    if request.POST:
        form = BookingForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "You have successfully booked for a clean service!")
            obj = form.data
            message = f"Hi {obj['name']}!  You have successfully booked a {CleanService.objects.get(id=obj['package'])} clean service scheduled for {obj['date']}."
            #message_html = render_to_string('snippets/email.html', {'name': obj['name'], 'package': CleanService.objects.get(id=obj['package']), 'date': obj['date']})
            subject = 'Notification from SneakSaver'
            send_email_view(email=obj['email'], subject=subject, message=message)
            return redirect('index')
        else:
            context['form'] = form
    context = {
        "service": CleanService.objects.all()
    }
    return render(request, "sneaksaver/booking.html", context)

def about_page_view(request):
    return render(request, "sneaksaver/about.html")

def contact_view(request):
    context = {}
    if request.POST:
        form = ContactForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for contacting us. We'll get back to you shortly!")
            obj = form.data
            message = f"Hi {obj['name']}! Thank you for contacting sneaksaver. We'll get back to you shortly!"
            subject = 'Notification from SneakSaver'
            send_email_view(obj['email'], subject, message)
            return redirect('index')
        else:
            context['form'] = form

    return render(request, "sneaksaver/contact.html")

def message_agent_view(request):
    if request.method == "POST":
        message = request.POST['message']
        Message(user=request.user.user_profile, message=message)
        message_list = Message.objects.all().filter(user=request.user.user_profile)
    context = {
        "message":list(message_list)
    }
    return JsonResponse(context, safe=False)