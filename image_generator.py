import os
import numpy as np
from PIL import Image
import random
import decimal
import application_constants
import application_functions
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen, urlretrieve
import re
from time import sleep
import random

""" -------------------------------------------------------------------------
    Randomly zooms in on the two images to further enshittify
    -------------------------------------------------------------------------"""

def zoom_random(images):
    zoom = float(decimal.Decimal(random.randrange(100, 200)) / 100)
    x = random.randint(30, 90)
    y = random.randint(50, 130)
    return_images = []
    for img in images:
        w, h = img.size
        zoom2 = zoom * 2
        img = img.crop((x - w / zoom2, y - h / zoom2, x + w / zoom2, y + h / zoom2))
        return_images.append(img.resize((w, h), Image.LANCZOS))
    return return_images


""" -------------------------------------------------------------------------
    Grabs two random player headshots from the 
    baseball-reference.com/players/a-z lists
    -------------------------------------------------------------------------"""

def download_two_random_bbref_headshots():
    # creates URL of a players page of a random letter, e.g. https://www.baseball-reference.com/players/a/
    request_url = (
        application_constants.BBREF_BASE_PLAYERS_URL
        + application_functions.generate_random_letter()
    )
    main_req = Request(request_url)
    html_page = urlopen(main_req).read()
    soup = BeautifulSoup(html_page, "html.parser")

    # find all link tags with an href of a baseball player, i.e. toss out random links on the page
    player_links = soup.findAll("a", attrs={"href": re.compile("^/players/.{5,}")})

    # shuffle the order of the links
    random.shuffle(player_links)

    # loop through these two links and navigate to each respective page
    links_with_headshots = 0
    for link in player_links:
        name = link.get_text()
        link_href = link.get("href")
        full_link = application_constants.BBREF_BASE_URL + link_href
        player_req = Request(full_link)
        player_page = urlopen(player_req).read()
        player_soup = BeautifulSoup(player_page, "html.parser")

        # find the correct image tag and download
        headshot_tag = player_soup.find(
            "img", attrs={"src": re.compile("^https://www.baseball-reference.com/.*mlbam.jpg$")}
        )
        if headshot_tag:
            links_with_headshots += 1
            print(name)
            print(headshot_tag.get("src"))
            urlretrieve(
                headshot_tag.get("src"),
                application_constants.PLAYER_HEADSHOTS_PATH + r"/" + name + ".jpg",
            )
            # sleep to avoid rate limit on bbref
            sleep(2)

        if links_with_headshots == 2:
            break


""" -------------------------------------------------------------------------
    Grabs two random archived player headshots 
    in the case of an error downloading from bbref
    -------------------------------------------------------------------------"""

def build_player_image():
    image_files = None
    images = None
    try:
        # empty folder of player headshots
        application_functions.empty_folder(application_constants.PLAYER_HEADSHOTS_PATH)

        # download two random headshots from bbref and open those files as images
        download_two_random_bbref_headshots()

        # resize the images
        application_functions.resize_images_in_directory(
            application_constants.PLAYER_HEADSHOTS_PATH,
            application_constants.DEFAULT_IMAGE_WIDTH,
            application_constants.DEFAULT_IMAGE_HEIGHT,
        )

        image_files = application_functions.get_random_files_from_directory(
            application_constants.PLAYER_HEADSHOTS_PATH, 2
        )
        images = [
            Image.open(
                os.path.join(application_constants.PLAYER_HEADSHOTS_PATH, file)
            ).convert("RGB")
            for file in image_files
        ]
    except Exception as e:
        # in the case of an exception,
        # use two files from the backup archive and open those files as images
        print(e)
        image_files = application_functions.get_random_files_from_directory(
            application_constants.PLAYER_HEADSHOTS_ARCHIVE_PATH, 2
        )
        images = [
            Image.open(
                os.path.join(application_constants.PLAYER_HEADSHOTS_ARCHIVE_PATH, file)
            ).convert("RGB")
            for file in image_files
        ]

    # open the 2 images and store in list
    images = zoom_random(images)

    # convert to numpy array
    image_arrays = np.array([np.array(image) for image in images], dtype=np.float32)

    # calculate the average
    average_array = np.mean(image_arrays, axis=0)

    # convert back to image
    average_image = Image.fromarray(np.uint8(average_array))

    # save image
    average_image.save(application_constants.OUTPUT_HEADSHOT_STATIC_PATH)
