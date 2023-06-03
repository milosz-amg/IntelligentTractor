import torch
import torchvision
from PIL import Image
import torch.nn as nn
from torch.optim import Adam
from torch.autograd import Variable
from torch.utils.data import DataLoader

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
classes = ['carrot', 'potato', 'wheat']

train_path = 'assets/learning/train'
test_path = 'assets/learning/test'

transformer = torchvision.transforms.Compose([
    torchvision.transforms.Resize((150, 150)),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
])

class Net(nn.Module):
    def __init__(self, num_classes=3):
        super(Net, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 12, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(12),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(12, 20, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(20, 32, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU()
        )
        self.classifier = nn.Linear(32 * 75 * 75, num_classes)

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x

def train(dataloader, model, optimizer, loss_fn):
    model.train()
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        optimizer.zero_grad()
        pred = model(X.float())
        loss = loss_fn(pred, y)
        loss.backward()
        optimizer.step()

        if batch % 5 == 0:
            current = batch * len(X)
            print(f"loss: {loss.item():>7f}  [{current:>5d}/{size:>5d}]")

def test(dataloader, model, loss_fn):
    model.eval()
    size = len(dataloader.dataset)
    test_loss, correct = 0, 0

    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X.float())
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).sum().item()

    test_loss /= size
    accuracy = 100.0 * correct / size
    print(f"Test Error:\n Accuracy: {accuracy:.1f}%, Avg loss: {test_loss:.8f}\n")

