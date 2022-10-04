from statistics import mode
import tensorflow as tf
import pandas as pd
import numpy as np
from PIL import Image
import cv2 as cv
from matplotlib.image import imread
from tensorflow.keras.models import load_model


model = load_model('models/model_110/')
# x,y=None,None
def load_image(file):
    img = Image.open(file)
    img = img.resize((64,64))
    x = np.array(img)
    return x

def evaulate(x):
    y = model.predict(np.array([x])
    return y


def get_prediction(x):
    k = np.argmax(model.predict(np.array([x])),axis=-1)[0]
    return k