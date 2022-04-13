import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np


def body_classification(img_path,model):

    img = image.load_img(img_path, target_size=(180, 180))
    img_array = image.img_to_array(img)
    img_preprocessed = np.expand_dims(img_array, axis=0)

    predictions = model(img_preprocessed)

    label = np.argmax(predictions, axis=1)[0]
    decoder = {0:'Cargo Van', 1:'Convertible', 2:'Coupe', 3:'Crossover', 4:'Hatchback', 5:'Minivan', 6:'Pickup', 7:'Roadster', 8:'SUV', 9:'Sedan', 10:'Wagon'}
    decoded_label = decoder[label]
    return decoded_label

















