from collections import OrderedDict

import numpy as np
import matplotlib.pyplot as plt

from torch import nn
from torch import optim
import torch.nn.functional as F

from torchvision import datasets, transforms

class Network(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 400)
        self.fc2 = nn.Linear(400, 200)
        self.fc3 = nn.Linear(200, 100)
        self.fc4 = nn.Linear(100, 10)

    def forward(self, x):
        layer1 = self.fc1(x)
        act1 = F.relu(layer1)
        layer2 = self.fc2(act1)
        act2 = F.relu(layer2)
        layer3 = self.fc3(act2)
        act3 = F.relu(layer3)
        layer4 = self.fc4(act3)
        act4 = F.softmax(layer4, dim=1)
        return act4