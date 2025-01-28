"""
TODO: Insert what this program does here.
"""

import sys
import requests
from PIL import Image

def get_img_prediction(
    server_ip: str, server_port: int, api_path: str, image_path: str
) -> str:
    """Send image to server for prediction."""
    # TODO: Replace with code to send image to server

    url = f"http://{server_ip}:{server_port}/{api_path}"
    img = Image.open(image_path).tobytes() # convert image to bytes
    prediction = requests.post(url, img) # post a request to the server

    return prediction.text


def main(server_ip: str, server_port: int) -> None:
    """Repeatedly prompt the user for a path to an image
    and send it to the server for prediction.
    Then display the result to the user.
    """
    # TODO: Replace with prompt to user and call to get_img_prediction
    print(f"Using server {server_ip}:{server_port}")
    api_path = "/predict"
    
    while True:
        img_path = input("Enter a path to an image: ")
        print(f"img_path {img_path}")

        get_img_prediction(server_ip, server_port, api_path, img_path)

if __name__ == "__main__":
    # Ensure user passes required arguments
    if len(sys.argv) != 3:
        print("Usage: python client.py <server IP address> <server port>")
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]))


