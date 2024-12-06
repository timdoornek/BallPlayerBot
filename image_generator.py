import os
import numpy as np
from PIL import Image
import random
import decimal
from application_constants import PLAYER_HEADSHOT_RESIZED_PATH, OUTPUT_HEADSHOT_PATH

def zoom_random(images):
    zoom = float(decimal.Decimal(random.randrange(100, 200))/100)
    x = random.randint(30,90)
    y = random.randint(50,130)
    return_images = []
    for img in images:
        w, h = img.size
        zoom2 = zoom * 2
        img = img.crop((x - w / zoom2, y - h / zoom2, 
                        x + w / zoom2, y + h / zoom2))
        return_images.append(img.resize((w, h), Image.LANCZOS))
    return return_images

def build_player_image():
    #list all image files in the player headshot directory and grab a random selection of 2
    image_files = [f for f in os.listdir(PLAYER_HEADSHOT_RESIZED_PATH) if os.path.isfile(os.path.join(PLAYER_HEADSHOT_RESIZED_PATH, f))]
    random_files = random.sample(image_files, 2)

    #open the 2 images and store in list
    images = [Image.open(os.path.join(PLAYER_HEADSHOT_RESIZED_PATH, file)).convert('RGB') for file in random_files]
    images = zoom_random(images)

    #convert to numpy array
    image_arrays = np.array([np.array(image) for image in images], dtype=np.float32)

    #calculate the average
    average_array = np.mean(image_arrays, axis=0)

    #convert back to image
    average_image = Image.fromarray(np.uint8(average_array))

    #save image
    average_image.save(OUTPUT_HEADSHOT_PATH)

    #display
    average_image.show()

    return OUTPUT_HEADSHOT_PATH