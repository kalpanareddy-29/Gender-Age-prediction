import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import cv2
from tensorflow.keras.models import load_model

# Load the pre-trained model
model = load_model('age_gender.h5')

# Function to preprocess the image
def preprocess_image(image_path, target_size=(48, 48)):
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Image could not be loaded.")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, target_size)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

# Function to predict age and gender
def predict_age_and_gender(image_path):
    preprocessed_image = preprocess_image(image_path)
    predictions = model.predict(preprocessed_image)
    age_prediction = predictions[1][0]  # Assuming age is the second output
    gender_prediction = np.argmax(predictions[0], axis=-1)[0]  # Assuming gender is the first output
    return age_prediction, gender_prediction

# Function to handle file upload and prediction
def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            age, gender = predict_age_and_gender(file_path)
            gender_str = 'Female' if gender == 1 else 'Male'
            image = Image.open(file_path)
            image = image.resize((200, 200), Image.ANTIALIAS)
            img_display = ImageTk.PhotoImage(image)

            # Update GUI with the results
            img_label.config(image=img_display)
            img_label.image = img_display
            result_label.config(text=f"Predicted Age: {age:.2f}\nPredicted Gender: {gender_str}")
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {e}")

# Create the main application window
root = tk.Tk()
root.title("Age and Gender Prediction")

# Create and place widgets
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

img_label = tk.Label(root)
img_label.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)

# Run the application
root.mainloop()
