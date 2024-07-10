import os
import sys
import numpy as np
import joblib
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import warnings

# Suppress warnings for model version inconsistency
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Function to preprocess and predict
def process_image(img_path, model):
    try:
        # Load and preprocess the image
        img = image.load_img(img_path, target_size=(150, 150))  # Match your model input size
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Rescale pixel values

        # Make a prediction
        prediction = model.predict(img_array)
        print(prediction)  # Print the prediction result

        # Determine and print the class label
        if prediction[0][0] > 0.5:
            print('Prediction: Malignant')
        else:
            print('Prediction: Benign')
    
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Incorrect number of arguments")
        print("Usage: python breast_cancer_prediction.py <image_path>")
        sys.exit(1)

    # Get the directory of the current script
    script_dir = os.path.dirname(__file__)

    # Define the path to the model file
    model_path = os.path.join(script_dir, 'bcd_model.pkl')

    # Load the model
    try:
        with open(model_path, 'rb') as f:
            model = joblib.load(f)
    except Exception as e:
        print(f"Error loading model: {e}")
        sys.exit(1)

    # Get the image path from command line argument
    image_path = sys.argv[1]

    # Verify if the image path exists
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found.")
        sys.exit(1)

    # Process the image and make a prediction
    process_image(image_path, model)
