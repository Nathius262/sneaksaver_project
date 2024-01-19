from django.shortcuts import render
import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.resnet50 import preprocess_input
import os
from django.conf import settings

# Load the trained model
file_path = os.path.join(settings.BASE_DIR, "sneakers_image_recog", "ml_model", 'sneak_image_recog_model.h5')

model = load_model(file_path)
index_to_label = {
    0: 'nike',
    1: 'converse',
    2: 'adidas',
    # Add more classes as needed
}



def preprocess_image(img):
    # Resize the image to the input size expected by the model
    input_shape = (240, 240)  # Adjust this according to your model's input size
    img = cv2.resize(img, input_shape)

    # Normalize the image pixel values to be in the range [0, 1]
    img = img / 255.0

    # Apply model-specific preprocessing, if any
    # For example, if you are using a pre-trained model like ResNet50
    img = preprocess_input(img)

    return img


def classify_sneaker(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image'].read()
        nparr = np.frombuffer(image, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Preprocess the image
        preprocessed_img = preprocess_image(img)

        # Make predictions using the loaded model
        #predictions = model.predict(np.expand_dims(preprocessed_img, axis=0))
        preprocessed_img_with_batch = np.expand_dims(preprocessed_img, axis=0)
        predictions = model.predict(preprocessed_img_with_batch)


        # Get the predicted class
        predicted_class = np.argmax(predictions)
        class_name = index_to_label[predicted_class]
        print(class_name)

        return render(request, 'model/prediction.html', {'class_name': class_name})

    return render(request, 'model/prediction.html')
