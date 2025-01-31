"""
Accepts an image path, sends a post request of this image to a server and waits for a response
"""

import sys
import requests
from PIL import Image


def get_img_prediction(
    server_ip: str, server_port: int, api_path: str, image_path: str
) -> str:
    """Send image to server for prediction."""
    url = f"http://{server_ip}:{server_port}/{api_path}"
    prediction = None
    try:
        files = {"file": (image_path, open(image_path, "rb"), "img/png")}

        prediction = requests.post(url, files=files)  # post a request to the server
        prediction = prediction.text
    except Exception as e:
        print(f"Error posting request: {e}")

    return prediction


def main(server_ip: str, server_port: int) -> None:
    """Repeatedly prompt the user for a path to an image
    and send it to the server for prediction.
    Then display the result to the user.
    """
    print(f"Using server {server_ip}:{server_port}")
    api_path = "/predict"

    while True:
        img_path = input("Enter a path to an image: ")
        print(f"img_path {img_path}")

        prediction = get_img_prediction(server_ip, server_port, api_path, img_path)
        print(prediction)


if __name__ == "__main__":
    # Ensure user passes required arguments
    if len(sys.argv) != 3:
        print("Usage: python client.py <server IP address> <server port>")
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]))
