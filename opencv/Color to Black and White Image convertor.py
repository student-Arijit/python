import streamlit as st
import cv2

st.header("Color to Black & White Convertion:")
image = st.file_uploader("upload image here")
if image is not None:
    try:
        st.image(image, "your image")
        with open("input.jpg", "wb") as f:
            f.write(image.getbuffer())

        img = cv2.imread("input.jpg")
        if img is not None:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            success = cv2.imwrite("output.jpg",gray)
            if success:
                st.success("Converted Successfully")
                st.subheader("Converted Image:")
                st.image("output.jpg", "Black & white image")
            else:
                st.error("Image is not converted")
        else:
            st.write("Image is not loading...")

    except AttributeError:
        st.write("No Image Provided or Image not Loading")
else:
    st.write("no image provided")
