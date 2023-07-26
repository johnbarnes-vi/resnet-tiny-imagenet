# Convolutional Neural Networks for Image Classification

This repository contains the implementation of several Convolutional Neural Network (CNN) models, including simple CNNs and ResNet models, for image classification tasks using the Tiny ImageNet dataset.

## Table of Contents
- [Dataset](#dataset)
- [Repository Structure](#repository-structure)
- [Models](#models)
  - [Simple CNN](#simple-cnn)
  - [Simple CNN with 256 Neurons](#simple-cnn-with-256-neurons)
  - [ResNet-18](#resnet-18)
  - [ResNet-34](#resnet-34)
- [Usage](#usage)
  - [Data Preprocessing](#data-preprocessing)
- [Contributing](#contributing)
- [License](#license)

## Dataset

The models implemented in this repository are trained on the Tiny ImageNet dataset. The dataset consists of 100,000 training images, 10,000 validation images, and 10,000 test images distributed across 200 classes. Each image is of the size 64x64 pixels with three color channels (RGB). For more details on the structure and content of the Tiny ImageNet dataset, refer to [`dir_structure.md`](tiny-imagenet-200/dir_structure.md).

## Repository Structure

The repository consists of several Python scripts, each implementing a different CNN model, and a Jupyter notebook that includes code for loading data, preprocessing it, and training and evaluating the models.

- `main.ipynb`: A Jupyter notebook that contains the main pipeline for loading the dataset, preprocessing it, training the models, and evaluating their performance.

- `cnn.py`: Defines a simple CNN model with two convolutional layers and two fully connected layers.

- `cnn256.py`: Defines a simple CNN model similar to the one in `cnn.py` but with more neurons in the fully connected layers.

- `resnet18.py`: Defines a ResNet-18 model, a deep CNN model known for its residual connections.

- `resnet34.py`: Defines a ResNet-34 model, a deeper variant of the ResNet-18 model.

## Models

This repository includes several types of CNN models designed for image classification tasks with 200 classes.

### Simple CNN

A basic CNN model with two convolutional layers followed by two fully connected layers. The model includes dropout layers for regularization.

### Simple CNN with 256 Neurons

A variant of the simple CNN model but with more neurons in the fully connected layers, making it potentially more suitable for slightly more complex tasks.

### ResNet-18

A deep CNN model known for its residual connections, which help to address the vanishing gradient problem in deep neural networks. The model includes several sets of basic blocks, each consisting of two convolutional layers with batch normalization and a ReLU activation function.

### ResNet-34

A deeper variant of the ResNet-18 model with more basic blocks, potentially making it suitable for even more complex tasks.

## Usage

### Data Preprocessing

Before training the models, the validation images in the Tiny ImageNet dataset need to be reorganized. This can be done by running the `data-prep.py` script, which reads the validation annotations file and moves each image into a subdirectory corresponding to its class.

## Contributing

Contributions are welcome!

## License

This project is licensed under the terms of the MIT license.

