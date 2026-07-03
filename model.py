import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader

class CNN(nn.Module):


    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv2d(
            in_channels=3,
            out_channels=32,
            kernel_size=3,
            stride=1,
            padding=1
        )
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(
                in_channels=32,
                out_channels=64,
                kernel_size=3,
                stride=1,
                padding=1
        )
        self.fc1 = nn.Linear(
    in_features=64 * 37 * 37,
    out_features=128
)
        self.fc2 = nn.Linear(in_features=128, out_features=6)


    def forward(self, x):
      
      x = self.conv1(x)
      x = self.relu(x)
      x = self.pool(x)

      x = self.conv2(x)
      x = self.relu(x)
      x = self.pool(x)

      x = x.flatten(start_dim=1)

      x = self.fc1(x)
      x = self.relu(x)
      x = self.fc2(x)
      return x


