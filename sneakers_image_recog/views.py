from django.http import JsonResponse
from django.shortcuts import render
from sneaksaver.models import CleanService, ShoeModel
import joblib
import os
from django.conf import settings
from .utils import image_augmentation



def classify_sneaker(request):
    model_filename =  os.path.join(settings.BASE_DIR, "sneakers_image_recog", "ml_model", "decision_tree_model.joblib")
    if request.method == 'POST':
        image = request.FILES['image'] or None
        
        augmented_image = image_augmentation(image)        
        loaded_model = joblib.load(model_filename)        
        Categories = ["nike","converse","adidas"]
        # Now, you can use the loaded_model for predictions
        # Assuming augmented_image is a 3D array, and you want to flatten it
        flattened_image = augmented_image.flatten()
        # Now you can pass the flattened image to the classifier
        predictions = loaded_model.predict([flattened_image])
        # Get the predicted index
        predicted_index = predictions[0]
        # Map the predicted index to the corresponding category name
        predicted_label = Categories[predicted_index]
        
        try:
            price_standard= CleanService.objects.get(service_name__icontains="standard")
        except CleanService.DoesNotExist:
            price_standard = 0.00
            
        try:
            product_model = ShoeModel.objects.get(name__icontains=str(predicted_label))
        except ShoeModel.DoesNotExist:
            pass


        context ={
            'model': product_model.name, 
            "model_price": product_model.price,
            'service_price': price_standard.service_price,
            'recommended':price_standard.service_name
        }
        return JsonResponse(context, safe=False)

    return render(request, 'model/prediction.html')
