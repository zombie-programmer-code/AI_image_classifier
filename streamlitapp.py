import streamlit as st
from PIL import Image, ImageOps

st.title("Predicting whether an image is real or if it is AI-generated")
uploaded_file = st.file_uploader("Upload a real or an AI-generated image",type=['png','jpg','jpeg'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    if st.button("Check"):
        result = predict(image)
