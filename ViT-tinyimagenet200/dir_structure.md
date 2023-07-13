# Tiny ImageNet Dataset Structure and Content Guide

This guide summarizes the directory structure, file naming conventions, and content of the Tiny ImageNet dataset as used in the `ViT-tinyimagenet200/` project.

## Directory Structure and Naming Conventions

The Tiny ImageNet dataset is contained in a directory named `tiny-imagenet-200/`, which includes the following:

- Three subdirectories: `train/`, `test/`, and `val/`.
- Two text files: `wnids.txt` and `words.txt`.

### `train/` Directory

The `train/` directory contains 200 subdirectories, each named with a unique WordNet ID (wnid). Each of these subdirectories includes:

- An `images/` subdirectory containing 500 JPEG images. The images are named `{wnid}_i.JPEG`, where `i` ranges from 0 to 499.
- A `{wnid}_boxes.txt` file containing bounding box information for the images.

### `test/` Directory

The `test/` directory contains an `images/` subdirectory with 10,000 JPEG images named `test_i.JPEG`, where `i` ranges from 0 to 9999.

### `val/` Directory

The `val/` directory contains:

- An `images/` subdirectory with 10,000 JPEG images named `val_i.JPEG`, where `i` ranges from 0 to 9999.
- A `val_annotations.txt` file containing class labels for the validation images.

## Content of Text Files

- `wnids.txt`: Contains the WordNet IDs (wnids) of the 200 classes in the dataset, one per line.
- `words.txt`: Contains the class labels (descriptions) corresponding to the WordNet IDs. Each line is in the format `{wnid}\t{description}`.
- `{wnid}_boxes.txt`: These files in the `train/` directories contain the bounding boxes for the objects in the training images. Each line is in the format `{filename}\t{x}\t{y}\t{h}\t{w}`.
- `val_annotations.txt`: This file in the `val/` directory contains the class labels for the validation images. Each line is in the format `{filename}\t{wnid}\t{x}\t{y}\t{h}\t{w}`.

## Data Arrangement

The dataset is divided into training, validation, and test sets. Each set is stored in its own subdirectory (`train/`, `val/`, and `test/` respectively). The training set is further divided into classes, each stored in its own subdirectory under `train/`.

## Assumptions for the Code

- The Tiny ImageNet dataset is not included in the repository due to its large size and needs to be downloaded manually.
- The code in the `ViT-tinyimagenet200/` directory assumes that the Tiny ImageNet dataset is placed in a `tiny-imagenet-200/` subdirectory under `ViT-tinyimagenet200/`.
