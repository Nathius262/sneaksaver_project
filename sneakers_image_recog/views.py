from django.http import JsonResponse
from django.shortcuts import render
from sneaksaver.models import CleanService

def classify_sneaker(request):
    if request.method == 'POST':
        image = request.FILES['image'] or None
        try:
            price_standard= CleanService.objects.get(service_name__icontains="standard")
        except CleanService.DoesNotExist:
            price_standard = 0.00
        context ={
            'model': "nike", 
            'price': price_standard.service_price,
            'recommended':price_standard.service_name
        }
        return JsonResponse(context, safe=False)

    return render(request, 'model/prediction.html')
