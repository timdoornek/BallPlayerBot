import os
from PIL import Image

# Specify the directory containing the images
image_directory = './player_headshots'
resized_directory = './player_headshots_resized'

# Create the directory for resized images if it doesn't exist
os.makedirs(resized_directory, exist_ok=True)

# List all image files in the directory
image_files = [f for f in os.listdir(image_directory) if os.path.isfile(os.path.join(image_directory, f))]

# Define the target size
target_size = (120, 180)

# Iterate over all image files and resize them
for image_file in image_files:
    try:
        # Open the image
        image_path = os.path.join(image_directory, image_file)
        image = Image.open(image_path)

        # Resize the image
        resized_image = image.resize(target_size)

        # Save the resized image to the new directory
        resized_image_path = os.path.join(resized_directory, image_file)
        resized_image.save(resized_image_path)

        print(f"Resized and saved {image_file} to {resized_image_path}")
    except Exception as e:
        print(f"Error processing {image_file}: {e}")