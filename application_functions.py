from re import *
import random
import string
import os
import shutil
from PIL import Image

""" -------------------------------------------------------------------------
    Pluralize a word from a singular input.
    Mostly works but English is dumb so there are plenty of exceptions.
    Really didn't wanna use a complicated library -- might even be funnier
    with mistakes.
    -------------------------------------------------------------------------"""

def pluralize_word(word):
    result = ""

    # Check if word is ending with s,x,z or is
    # ending with ah, eh, ih, oh,uh,dh,gh,kh,ph,rh,th
    # add es
    if search("[sxz]$", word) or search("[^aeioudgkprt]h$", word):
        result = sub("$", "es", word)
    # Check if word is ending with ay,ey,iy,oy,uy
    # remove y add ies
    elif search("[aeiou]y$", word):
        result = sub("y$", "ies", word)
    # In all the other cases
    # add s
    else:
        result = word + "s"

    return result


""" -------------------------------------------------------------------------
    Generate a random a-z letter.
    -------------------------------------------------------------------------"""

def generate_random_letter():
    return random.choice(string.ascii_lowercase)


""" -------------------------------------------------------------------------
    Delete all files in a folder.
    -------------------------------------------------------------------------"""

def empty_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print("Failed to delete %s. Reason: %s" % (file_path, e))


""" -------------------------------------------------------------------------
    X amount of random files from directory.
    -------------------------------------------------------------------------"""

def get_random_files_from_directory(folder_path, num_files):
    return random.sample(
        [
            f
            for f in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, f))
        ],
        num_files,
    )


""" -------------------------------------------------------------------------
    Resize all image files in directory to specified w/h
    -------------------------------------------------------------------------"""

def resize_images_in_directory(folder_path, width, height):
    # List all image files in the directory
    image_files = [
        f
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]

    # Define the target size
    target_size = (width, height)

    # Iterate over all image files and resize them
    for image_file in image_files:
        try:
            # Open the image
            image_path = os.path.join(folder_path, image_file)
            image = Image.open(image_path).convert('RGB')

            # Resize the image
            resized_image = image.resize(target_size)

            # Save the resized image to the new directory
            resized_image_path = os.path.join(folder_path, image_file)
            resized_image.save(resized_image_path)

            print(f"Resized and saved {image_file} to {resized_image_path}")
        except Exception as e:
            print(f"Error processing {image_file}: {e}")
            raise e
