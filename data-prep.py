import os
import shutil

path_to_dataset = "./tiny-imagenet-200"

# Path to the validation annotations file
val_annotations_path = os.path.join(path_to_dataset, "val/val_annotations.txt")

# Create a dictionary mapping from image names to WordNet IDs
image_to_wnid = {}

with open(val_annotations_path, "r") as f:
    for line in f:
        image_name, wnid = line.split("\t")[:2]
        image_to_wnid[image_name] = wnid

# Path to the directory containing the validation images
val_images_dir_path = os.path.join(path_to_dataset, "val/images")

# Iterate over all validation images
for image_name in os.listdir(val_images_dir_path):
    # Get the corresponding WordNet ID for the image
    wnid = image_to_wnid.get(image_name)
    
    # Create a new directory for the WordNet ID, if it doesn't exist already
    new_dir_path = os.path.join(path_to_dataset, f"val/{wnid}")
    os.makedirs(new_dir_path, exist_ok=True)

    # Move the image to the new directory
    old_image_path = os.path.join(val_images_dir_path, image_name)
    new_image_path = os.path.join(new_dir_path, image_name)
    shutil.move(old_image_path, new_image_path)
