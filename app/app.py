
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Smart Waste Classification",
    page_icon="♻️",
    layout="centered"
)

st.title("♻️ Smart Waste Classification")
st.write("Upload a waste image to classify it.")

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "waste_classifier.keras"
)

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

uploaded_file = st.file_uploader(
    "Upload Waste Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded Image", width=300)

    image = image.resize((128, 128))

    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)

    prediction = model.predict(image_array)[0][0]

    if prediction >= 0.5:
        category = "Recyclable Waste"
        confidence = prediction * 100
    else:
        category = "Organic Waste"
        confidence = (1 - prediction) * 100

    st.success(f"Prediction: {category}")
    st.metric("Confidence", f"{confidence:.2f}%")
