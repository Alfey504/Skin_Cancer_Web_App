import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image

def read_image(imgname):

    image = np.asarray(Image.open(imgname).resize((100,75)))
    return image

def predict_x(x):
    
    model = keras.models.load_model('model/model_trained.h5')
    p = model.predict(x)
    return p

def classify(imgname):

    image = read_image("static/uploads/"+imgname)
    x = image.reshape(-1, *(75, 100, 3))
    x = (x - 159.88411714650246)/46.45448942251337
    p = predict_x(x)
    pr = p[0].tolist()
    return pr

