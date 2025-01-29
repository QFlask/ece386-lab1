"""
TODO: Insert what this program does here. Should start with
digits is a FastAPI app that...
"""

from PIL import Image, ImageOps
from io import BytesIO
from fastapi import FastAPI, File, UploadFile
import tensorflow as tf
from tensorflow import keras
import numpy as np
from typing import Annotated

model_path: str = "digits.keras"

model = tf.keras.models.load_model(model_path)  # load trained model object

app = FastAPI()  # create FastAPI app


def image_to_np(image_bytes: bytes) -> np.ndarray:
    """Convert image to proper numpy array"""
    # First must use pillow to process bytes
    img = Image.open(BytesIO(image_bytes))
    img = ImageOps.grayscale(img)  # grayscale image
    img = img.resize((28, 28))  # resize the image to 28x28 px

    img = np.array(img)  # convert img to numpy array
    return img


# accepts posts requests of bytes to /predict
@app.post("/predict")
async def get_request(file: Annotated[bytes, File()]):  # Annotated[bytes, File()]):
    image = image_to_np(file)
    image = tf.expand_dims(image, axis=0)  # shape (1, 28, 28) for model
    prediction = model.predict(image)  # get a prediction
    return {"prediction": str(prediction.argmax())}  # return the predicted digit
