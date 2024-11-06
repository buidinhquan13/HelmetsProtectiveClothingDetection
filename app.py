# import streamlit as st
# from ultralytics import YOLO
# from PIL import Image
# import requests
# from io import BytesIO
# import cv2

# # Load mô hình YOLOv8
# model = YOLO("weights/best.pt")  # Hoặc "weights/last.pt"

# # Hàm để xử lý ảnh từ URL hoặc upload từ máy tính
# def load_image(image_file=None, image_url=None):
#     if image_url:
#         try:
#             response = requests.get(image_url)
#             img = Image.open(BytesIO(response.content))
#             return img
#         except Exception as e:
#             st.error(f"Error loading image from URL: {e}")
#             return None
#     elif image_file:
#         img = Image.open(image_file)
#         return img
#     else:
#         return None

# # Tạo giao diện cho ứng dụng Streamlit
# st.title("Demo Nhận Diện Nón và Áo Bảo Hộ")

# # Upload ảnh hoặc nhập URL
# image_source = st.radio("Chọn nguồn ảnh:", ("Upload ảnh", "Nhập URL"))

# image = None  # Khởi tạo biến image ở đầu chương trình để tránh lỗi NameError

# if image_source == "Upload ảnh":
#     uploaded_image = st.file_uploader("Tải lên ảnh", type=["jpg", "jpeg", "png", "webp"])
#     if uploaded_image:
#         st.image(uploaded_image, caption="Ảnh gốc", use_column_width=True)
#         image = load_image(image_file=uploaded_image)
# elif image_source == "Nhập URL":
#     image_url = st.text_input("Nhập URL của ảnh")
#     if image_url:
#         image = load_image(image_url=image_url)
#         if image:
#             st.image(image, caption="Ảnh gốc", use_column_width=True)

# # Dự đoán và hiển thị kết quả khi nhấn nút
# if image:
#     if st.button("Dự đoán"):
#         # Thực hiện dự đoán YOLOv8
#         results = model(image, conf=0.5)

#         # Vẽ kết quả dự đoán lên ảnh
#         annotated_image = results[0].plot()  # Vẽ bounding boxes lên ảnh
        
#         if annotated_image.shape[-1] == 3:  # Kiểm tra nếu ảnh là BGR
#             annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
#         else:
#             annotated_image_rgb = annotated_image
        
#         # Hiển thị ảnh kết quả bên phải
#         st.subheader("Kết quả dự đoán:")
#         st.image(annotated_image_rgb, caption="Ảnh với các đối tượng nhận diện", use_column_width=True)



##############################################
# import streamlit as st
# from ultralytics import YOLO
# from PIL import Image
# import requests
# from io import BytesIO
# import cv2

# # Load the YOLOv8 model
# model = YOLO("weights/best.pt")  # Or "weights/last.pt"

# # Function to load the image from URL or upload from computer
# def load_image(image_file=None, image_url=None):
#     if image_url:
#         try:
#             response = requests.get(image_url)
#             img = Image.open(BytesIO(response.content))
#             return img
#         except Exception as e:
#             st.error(f"Error loading image from URL: {e}")
#             return None
#     elif image_file:
#         img = Image.open(image_file)
#         return img
#     else:
#         return None

# # Create the UI for the application
# st.title("Demo Nhận Diện Nón và Áo Bảo Hộ")

# # Layout for choosing image source
# col1, col2 = st.columns([1, 2])

# with col1:
#     st.write("Chọn nguồn ảnh:")
#     image_source = st.radio("", ("Upload ảnh", "Nhập URL"))

# image = None

# if image_source == "Upload ảnh":
#     uploaded_image = st.file_uploader("Tải lên ảnh", type=["jpg", "jpeg", "png", "webp"])
#     if uploaded_image:
#         image = load_image(image_file=uploaded_image)
# elif image_source == "Nhập URL":
#     image_url = st.text_input("Nhập URL của ảnh")
#     if image_url:
#         image = load_image(image_url=image_url)

# # Show original and prediction images side by side
# col_left, col_right = st.columns(2)

# with col_left:
#     st.write("### Show Ảnh gốc")
#     if image:
#         st.image(image, caption="Ảnh gốc", use_column_width=True)
        
# with col_right:
#     st.write("### Show Ảnh predict")
#     if image and st.button("Dự đoán"):
#         # Perform YOLOv8 prediction
#         results = model(image, conf=0.5)

#         # Draw the prediction results on the image
#         annotated_image = results[0].plot()  # Draw bounding boxes on the image
        
#         if annotated_image.shape[-1] == 3:  # Check if image is BGR
#             annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
#         else:
#             annotated_image_rgb = annotated_image
        
#         # Display the prediction result image
#         st.image(annotated_image_rgb, caption="Ảnh với các đối tượng nhận diện", use_column_width=True)



#########################################

import streamlit as st
from ultralytics import YOLO
from PIL import Image
import requests
from io import BytesIO
import cv2

# Load YOLOv8 model
model = YOLO("weights/best.pt")  # Replace with your model path

# Function to load the image from URL or upload from computer
def load_image(image_file=None, image_url=None):
    if image_url:
        try:
            response = requests.get(image_url)
            img = Image.open(BytesIO(response.content))
            return img
        except Exception as e:
            st.error(f"Error loading image from URL: {e}")
            return None
    elif image_file:
        img = Image.open(image_file)
        return img
    else:
        return None

# Create the UI for the application
st.title("Demo Nhận Diện Nón và Áo Bảo Hộ")

# Layout for choosing image source
col1, col2 = st.columns([1, 2])

with col1:
    st.write("Chọn nguồn ảnh:")
    image_source = st.radio("", ("Upload ảnh", "Nhập URL"))

image = None

if image_source == "Upload ảnh":
    uploaded_image = st.file_uploader("Tải lên ảnh", type=["jpg", "jpeg", "png", "webp"])
    if uploaded_image:
        image = load_image(image_file=uploaded_image)
elif image_source == "Nhập URL":
    image_url = st.text_input("Nhập URL của ảnh")
    if image_url:
        image = load_image(image_url=image_url)

# Centered "Dự đoán" button
if st.button("Dự đoán") and image:
    # Perform YOLOv8 prediction
    results = model(image, conf=0.5)

    # Annotate image with prediction results
    annotated_image = results[0].plot()  # Draw bounding boxes on image

    # Convert to RGB if necessary
    if annotated_image.shape[-1] == 3:  # Check if image is BGR
        annotated_image_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
    else:
        annotated_image_rgb = annotated_image

    # Display the images in two columns
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("ảnh gốc")
        st.image(image, caption="Ảnh gốc", use_column_width=True)
    with col2:
        st.subheader("ảnh predict")
        st.image(annotated_image_rgb, caption="Ảnh với các đối tượng nhận diện", use_column_width=True)
