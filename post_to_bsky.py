from atproto import Client
from application_constants import BSKY_USERNAME, BSKY_PASSWORD

def post_to_bsky(text, image_path):
    client = Client()
    client.login(BSKY_USERNAME, BSKY_PASSWORD)

    with open(image_path, 'rb') as f:
        img_data = f.read()

    return client.send_image(text=text, image=img_data, image_alt=text)