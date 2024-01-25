from django.http import JsonResponse
from django.shortcuts import render

def classify_sneaker(request):
    if request.method == 'POST':
        image = request.FILES['image'] or None
        context ={
            'model': "nike", 
            'price': 14,
            'recommended':"standard"
        }
        return JsonResponse(context, safe=False)

    return render(request, 'model/prediction.html')
