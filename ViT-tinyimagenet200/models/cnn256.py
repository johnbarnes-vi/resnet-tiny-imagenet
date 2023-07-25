"""This is an implementation of a simple Convolutional Nueral Network with two dense layers of 512 neurons each"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np

class SimpleCNN256(nn.Module):
    def __init__(self):
        super(SimpleCNN256, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)  # Input channels = 3, output channels = 6, kernel size = 5
        self.pool = nn.MaxPool2d(2, 2)  # 2x2 max pooling
        self.conv2 = nn.Conv2d(6, 16, 5)  # Input channels = 6, output channels = 16, kernel size = 5
        self.fc1 = nn.Linear(16 * 13 * 13, 256)  # Fully connected layer
        self.dropout1 = nn.Dropout(0.25) # Dropout layer for overfitting
        self.fc2 = nn.Linear(256, 256)
        self.dropout2 = nn.Dropout(0.25) # Dropout layer for overfitting
        self.fc3 = nn.Linear(256, 200)  # 200 output classes

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))  # Convolution -> ReLU -> Pooling
        x = self.pool(F.relu(self.conv2(x)))  # Convolution -> ReLU -> Pooling
        x = x.view(-1, 16 * 13 * 13)  # Flatten the tensor
        x = F.relu(self.fc1(x))  # Fully connected -> ReLU
        x = self.dropout1(x)
        x = F.relu(self.fc2(x))  # Fully connected -> ReLU
        x = self.dropout2(x)
        x = self.fc3(x)  # Fully connected
        return x