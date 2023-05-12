# Medical-Image-Segmentation
Medical image segmentation is a crucial task in the field of medical imaging, which involves the identification of regions of interest in medical images, such as organs, tumors, and other abnormalities, by separating them from the surrounding tissue or background. The accurate segmentation of medical images is essential for diagnosis, treatment planning, and patient monitoring.

# Technologies Used
Streamlit, NumPy, cv2 (OpenCV), Pillow, PyCharm

# How to run 
1. Download the app.py and add it in a folder 
2. Open command propmt in that folder
3. run pip install streamlit in the command prompt
4. run streamlit run app.py (The app will be opened in the browser)
5. Use any Medical Image Dataset to test the app (I used the Sample NIH Chest X-ray Dataset - Keggle: https://www.kaggle.com/datasets/nih-chest-xrays/sample, Full dataset - Kaggle: https://www.kaggle.com/datasets/nih-chest-xrays/data)
6. In the browser grag and drpo or open the image location to add the image 
7. The output will we a binary image segmented on a Threshold based method
