import streamlit as st
import numpy as np
import cv2
from PIL import Image

# Function to read an image from file
def read_image(file):
    image = np.array(Image.open(file))
    return image

# Function to display an image in the app
def display_image(image):
    st.image(image, use_column_width=True)

# Function to process a medical image
def process_image(image):
    # read the input image
    img = cv2.imdecode(np.fromstring(image.read(), np.uint8), cv2.IMREAD_GRAYSCALE)

    # apply some preprocessing, such as smoothing and thresholding
    img_blur = cv2.GaussianBlur(img, (5, 5), 0)
    _, img_thresh = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # find contours in the thresholded image
    contours, _ = cv2.findContours(img_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # draw the contours on a black background
    img_contours = np.zeros_like(img)
    cv2.drawContours(img_contours, contours, -1, 255, 2)

    # stack the original image and the contours image horizontally
    output = np.hstack((img, img_contours))

    return output

# Main function
def main():
    st.write("<h1 style='text-align: center;'>Medical Image Segmentation</h1>", unsafe_allow_html=True)

    # Upload Image
    image = st.file_uploader("", type=['png', 'jpeg', 'jpg'])

    if image is not None:
        # Process the image
        output1 = process_image(image)

        # Display the processed image
        st.image(output1, use_column_width=True)

# Run the app
if __name__ == "__main__":
    main()
