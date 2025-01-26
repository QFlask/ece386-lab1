"""
TODO: Insert what this program does here. Should start with
digits is a FastAPI app that...
"""

from PIL import Image
from io import BytesIO
from fastapi import FastAPI
import tensorflow
from tensorflow import keras
import numpy as np

model_path: str = "digits.keras"

model = tf.keras.models.load_model(model_path) # load trained model object

app = FastAPI() # create FastAPI app

def image_to_np(image_bytes: bytes) -> np.ndarray:
    """Convert image to proper numpy array"""
    # First must use pillow to process bytes
    img = Image.open(BytesIO(image_bytes))
    # TODO: convert image to grayscale and resize
    img = tf.image.resize(img, [28,28]) # resize the image to 28x28 px    

    # TODO: convert image to numpy array of shape model expects
    img = keras.img_to_array(img) # convert to np array    
    img = keras.ops.image.rgb_to_grayscale(img) # grayscale np array

    return img


# TODO: Define predict POST function
@app.post("/predict") # what do i put here?
def fastapi_post():
    pass
