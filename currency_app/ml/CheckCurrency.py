import tensorflow as tf
from tensorflow import keras
import numpy as np
from currency_app.ml.TextToAudio import TextToAudio

class CheckCurrency:
    def checkCurrency(self, image):
        IMG_SIZE = 224

        try:
            model = keras.models.load_model("C:\\Users\\Rouna\\PycharmProjects\\CurrencyRecognizer\\currency_app\\ml\\models\\best_ResNet50.keras")
        except Exception as e:
            print("Error loading model: ", e)
            exit(0)

        class_names = ['10', '100', '20', '200', '2000', '50', '500', 'Background']

        try:
            image_bytes = image.read()
            image_tensor = tf.image.decode_image(image_bytes, channels=3)  # Ensure 3 channels
            image_tensor = tf.image.resize(image_tensor, (IMG_SIZE, IMG_SIZE))
            image_tensor = tf.expand_dims(image_tensor, axis=0)
        except Exception as e:
            print(f"Error processing image: {e}")
            exit(1)

        try:
            prediction = model(image_tensor, training=False)
            predicted_index = np.argmax(prediction[0])
            predicted_label = class_names[predicted_index]
            print(f"Predicted Label: {predicted_label}")
        except Exception as e:
            print(f"Error predicting image: {e}")
            exit(1)

        try:
            print("Calling TextToAudio.")
            return TextToAudio(predicted_label)
        except Exception as e:
            return TextToAudio(f"Error processing audio: {e}")

