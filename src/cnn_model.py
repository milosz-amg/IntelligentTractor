import torch
import torchvision
from PIL import Image
import torch.nn as nn
from torch.optim import Adam
from torch.autograd import Variable
from torch.utils.data import DataLoader


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
classes = ['carrot', 'potato', 'wheat']

train_path = ('assets/learning/train')

test_path = ('assets/learning/test')

transformer = torchvision.transforms.Compose([
    torchvision.transforms.Resize((150, 150)),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize([0.5, 0.5, 0.5],
                         [0.5, 0.5, 0.5])
])

class Net(nn.Module):
    def __init__(self, num_classes=6):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=12, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(num_features=12)
        self.relu1 = nn.ReLU()

        self.pool = nn.MaxPool2d(kernel_size=2)

        self.conv2 = nn.Conv2d(in_channels=12, out_channels=20, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()

        self.conv3 = nn.Conv2d(in_channels=20, out_channels=32, kernel_size=3, stride=1, padding=1)
        self.bn3 = nn.BatchNorm2d(num_features=32)
        self.relu3 = nn.ReLU()

        self.fc = nn.Linear(in_features=75 * 75 * 32, out_features=num_classes)

    def forward(self, input):
        output = self.conv1(input)
        output = self.bn1(output)
        output = self.relu1(output)

        output = self.pool(output)

        output = self.conv2(output)
        output = self.relu2(output)

        output = self.conv3(output)
        output = self.bn3(output)
        output = self.relu3(output)

        output = output.view(-1, 32 * 75 * 75)
        output = self.fc(output)

        return output


def train(dataloader, model: Net, optimizer: Adam, loss_fn: nn.CrossEntropyLoss):
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        pred = model(X.float())
        loss = loss_fn(pred, y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch % 5 == 0:
            loss, current = loss.item(), batch * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


def test(dataloader, model: Net, loss_fn: nn.CrossEntropyLoss):
    size = len(dataloader.dataset)
    model.eval()
    test_loss, correct = 0, 0

    with torch.no_grad():
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            pred = model(X.float())
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= size
    correct /= size
    print(f"Test Error: \n Accuracy: {(100 * correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")


def prediction(img_path, model: Net):
    image = Image.open(img_path).convert('RGB')
    image_tensor = transformer(image).float()
    image_tensor = image_tensor.unsqueeze_(0)

    if torch.cuda.is_available():
        image_tensor.cuda()
    input = Variable(image_tensor)
    output = model(input)

    index = output.data.numpy().argmax()
    pred = classes[index]
    return pred


def learn():
    num_epochs = 50

    train_loader = DataLoader(
        torchvision.datasets.ImageFolder(train_path, transform=transformer),
        batch_size=64, shuffle=True
    )
    test_loader = DataLoader(
        torchvision.datasets.ImageFolder(test_path, transform=transformer),
        batch_size=32, shuffle=True
    )

    model = Net(3).to(device)
    optimizer = Adam(model.parameters(), lr=1e-3, weight_decay=0.0001)
    loss_fn = nn.CrossEntropyLoss()

    for t in range(num_epochs):
        print(f"Epoch {t + 1}\n-------------------------------")
        train(train_loader, model, optimizer, loss_fn)
        test(test_loader, model, loss_fn)
    print("Done!")
    torch.save(model.state_dict(), f'plants.model')
