import pickle
from tensorflow.keras.models import model_from_json

# Function to save the model to a .pkl file
def save_model_to_pkl(model, file_path):
    # Serialize model to JSON
    model_json = model.to_json()
    # Serialize weights to HDF5
    model.save_weights("model_weights.h5")
    
    # Save the model architecture and weights
    with open(file_path, 'wb') as file:
        pickle.dump({'model_json': model_json, 'model_weights': "model_weights.h5"}, file)

# Function to load the model from a .pkl file
def load_model_from_pkl(file_path):
    # Load the model architecture and weights
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    
    # Load the model architecture
    model = model_from_json(data['model_json'])
    # Load weights into the model
    model.load_weights(data['model_weights'])
    
    return model

# Save the model to a .pkl file
save_model_to_pkl(model, './trained_lung_cancer_model.pkl')

# Load the model from the .pkl file (for verification)
loaded_model = load_model_from_pkl('./trained_lung_cancer_model.pkl')

# Compile the loaded model
loaded_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Verify that the loaded model is the same as the original model by printing the summary
loaded_model.summary()
