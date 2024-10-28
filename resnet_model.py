import torch
from torchvision import models, transforms
import torch.nn as nn
model = models.resnet50()
model.load_state_dict(torch.load('resnet50-0676ba61.pth'))
model.eval()
model.fc = nn.Sequential()
