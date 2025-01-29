# Digits Server

Accepts a post request of a white-on-black handwritten digit image, runs inference on the image and returns a prediction as a digit 0-9.

## Usage

1. cd to the ./server directory
2. Create a virtual environment "python3 -m venv .venv"
3. Activate the venv "source .venv/bin/activate"
4. Install required dependencies "pip install -r requirements.txt"
5. run the server with "fastapi run digits.py"
