import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model only once
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("model.h5")

model = load_model()
class_names = ["Normal", "Anomaly"]

st.title("🧠 Anomaly Detection App")
st.markdown("Upload an image or take a picture to check for anomalies.")

# ---- Image Upload Prediction ----
st.subheader("📁 Upload an Image")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption='Uploaded Image')

    img = image.resize((224, 224))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]

    st.write(f"### 🔍 Prediction: **{predicted_class}**")

# ---- Camera Input Prediction ----
st.markdown("---")
st.subheader("📸 Take a Picture (Streamlit Cloud Compatible)")

image_data = st.camera_input("Capture image")

if image_data is not None:
    image = Image.open(image_data).convert("RGB")
    st.image(image, caption="Captured Image")

    img = image.resize((224, 224))
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]

    st.write(f"### 🔍 Prediction: **{predicted_class}**")