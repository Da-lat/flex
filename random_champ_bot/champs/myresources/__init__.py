import glob
import os
from PIL import Image

MY_DIR = os.path.dirname(os.path.abspath(__file__))

CHAMPS_WITH_ROLE_DATA_FILENAME = "champs_by_role.txt"
with open(os.path.join(MY_DIR, CHAMPS_WITH_ROLE_DATA_FILENAME), "r") as f:
    CHAMPS_WITH_ROLE_DATA = f.read().split("\n")


CHAMP_IMAGES_FILENAMES = glob.glob(os.path.join(MY_DIR, "images/*"))
IMAGE_BY_CHAMP_ID = {}
for champ_image_filename in CHAMP_IMAGES_FILENAMES:
    IMAGE_BY_CHAMP_ID[os.path.basename(champ_image_filename).replace(".png", "")] = Image.open(champ_image_filename)

print(IMAGE_BY_CHAMP_ID.keys())
