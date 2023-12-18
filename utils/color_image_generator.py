# color_image_generator.py

import cv2
import numpy as np
import base64

def generate_color_image(red, green, blue, size):
    rgb_array = np.full((size, size, 3), (blue, green, red), dtype=np.uint8)
    _, img_encoded = cv2.imencode('.png', rgb_array)
    img_base64 = base64.b64encode(img_encoded).decode('utf-8')
    return img_base64
