#import modules

from google.colab import files
import os
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image as Img
import cv2
from skimage.transform import resize
print('Done!')

# change to images directory to upload image files
%cd /content/U-2-Net/images