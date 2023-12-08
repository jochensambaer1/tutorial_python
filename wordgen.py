import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the pre-trained model
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Define a function to classify an image
def classify_image(image_path):
    # Load and preprocess the image
    image = load_img(image_path, target_size=(224, 224))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = tf.keras.applications.mobilenet_v2.preprocess_input(image)

    # Make predictions
    predictions = model.predict(image)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)[0]

    # Print the top predictions
    for _, label, confidence in decoded_predictions:
        print(f"{label}: {confidence * 100}%")

# Example usage
image_path = "path/to/your/image.jpg"
classify_image(image_path)
