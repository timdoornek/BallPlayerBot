from atproto import Client

def post_to_bsky(text, image_path):
    client = Client()
    client.login('username_here', 'password_here')

    with open(image_path, 'rb') as f:
        img_data = f.read()

    return client.send_image(text=text, image=img_data, image_alt=text)