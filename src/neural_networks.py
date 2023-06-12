import torch
import torchvision
from PIL import Image
import torch.nn as nn
from torch.optim import Adam
from torch.autograd import Variable
from torch.utils.data import DataLoader

# Check if CUDA-enabled GPU is available and set the device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Define the classes for classification
classes = ['carrot', 'potato', 'wheat']

# Set the paths for the training and test data directories
train_path = 'assets/learning/train'
test_path = 'assets/learning/test'

#list of transforms to compose (lista przekształceń do utworzenia)
transformer = torchvision.transforms.Compose([
    # resize input image to the given size
    torchvision.transforms.Resize((150, 150)),
    # convert image to tensor(muli dim array)
    torchvision.transforms.ToTensor(),
    # normalize tensor image with wit mean and standard deviation
    # normalize doesn't support PIL image -> that is why we do .ToTensor before
    # output[channel] = (input[channel] - mean[channel]) / std[channel]
    torchvision.transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
])


class Net(nn.Module):
    def __init__(self, num_classes=3):
        super(Net, self).__init__()
        # Sequential - ordered dictionary
        # Define the convolutional layers
        # The output of one layer serves as the input to the next layer (3->12->20->32)
        self.features = nn.Sequential(
            # Applies a 2D convolution over an input signal composed of several input planes
            # Stosuje splot 2D dla sygnału wejściowego złożonego z kilku płaszczyzn wejściowych
            nn.Conv2d(3, 12, kernel_size=3, stride=1, padding=1),
            # parameter of torch.nn.BatchNorm2d is the number of dimensions/channels that output 
            # from the last layer and come in to the batch norm layer.
            nn.BatchNorm2d(12),
            # activation function relu(x) = { 0 if x<0, x if x > 0}
            # after each layer, an activation function needs to be applied
            # so as to make the network non-linear and fit complex data
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(12, 20, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.Conv2d(20, 32, kernel_size=3, stride=1, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU()
        )
        # takes the flattened feature maps from the previous convolutional layers as input
        self.classifier = nn.Linear(32 * 75 * 75, num_classes)

    def forward(self, x):
        # Forward pass through the network
        x = self.features(x)
        # Pass the input through the sequential block of 
        # convolutional layers and activation functions 
        x = x.view(x.size(0), -1)
        # Reshape the tensor by flattening it along the second dimension        
        x = self.classifier(x)
        # Pass the flattened tensor through the linear layer for classification
        return x
        # Return the output tensor

def train(dataloader, model, optimizer, loss_fn):
    model.train()
    size = len(dataloader.dataset)
    # Get the total number of training examples
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)
        # Move the input tensors to the appropriate device (CPU or GPU)        
        optimizer.zero_grad()
        # Clear the gradients of the model parameters        
        pred = model(X.float())
        # Perform a forward pass to obtain the predicted outputs       
        loss = loss_fn(pred, y)
        # Compute the loss between the predicted outputs and the ground truth labels        
        loss.backward()
        # Perform backpropagation to compute the gradients of the model parameters        
        optimizer.step()
        # Update the model parameters using the computed gradients        
        if batch % 5 == 0:
            current = batch * len(X)
            # Compute the current batch size            
            print(f"loss: {loss.item():>7f}  [{current:>5d}/{size:>5d}]")
            # Print the current loss and the progress of the training in material def accuracy

def test(dataloader, model, loss_fn):
    model.eval()
    # Set the model to evaluation mode    
    size = len(dataloader.dataset)
    # Get the total number of examples in the dataloader    
    test_loss, correct = 0, 0
    # Initialize variables to keep track of the total test 
    # loss and the number of correct predictions   
    with torch.no_grad():
        # Disable gradient computation        
        for X, y in dataloader:
            X, y = X.to(device), y.to(device)
            # Move the input tensors to the appropriate device (CPU or GPU)            
            pred = model(X.float())
            # Perform a forward pass to obtain the predicted outputs            
            test_loss += loss_fn(pred, y).item()
            # Compute the loss between the predicted outputs and the ground truth labels            
            correct += (pred.argmax(1) == y).sum().item()
            # Count the number of correct predictions
            
    test_loss /= size
    # Calculate the average test loss    
    accuracy = 100.0 * correct / size
    # Calculate the accuracy as a percentage    
    print(f"Test Error:\n Accuracy: {accuracy:.1f}%, Avg loss: {test_loss:.8f}\n")
    # Print the test accuracy and average test loss
    
def predict(img_path, model):
    image = Image.open(img_path).convert('RGB')
    # Open the image file from the given path and convert it to RGB mode    
    image_tensor = transformer(image).unsqueeze(0).to(device)
    # Apply the image transformation pipeline defined earlier and convert the image to a tensor
    # Add an extra dimension at the beginning to represent the batch
    # Move the image tensor to the appropriate device (CPU or GPU)    
    output = model(image_tensor)
    # Pass the image tensor through the model to obtain the output logits    
    _, predicted_idx = torch.max(output, 1)
    # Find the index of the predicted class by taking the maximum value along the second dimension    
    pred = classes[predicted_idx.item()]
    # Retrieve the corresponding class label from the classes list using the predicted index    
    return pred

def learn():
    num_epochs = 50
    batch_size = 64
    # Create a dataset from the images in the train_path directory
    train_dataset = torchvision.datasets.ImageFolder(train_path, transform=transformer)
    # Create a data loader for the train dataset to load data in batches
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    # Create a dataset from the images in the test_path directory
    test_dataset = torchvision.datasets.ImageFolder(test_path, transform=transformer)
    # Create a data loader for the test dataset to load data in batches
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=True)
    # Create an instance of the neural network model
    model = Net(len(classes)).to(device)
    # Create an optimizer for updating the model parameters during training
    optimizer = Adam(model.parameters(), lr=1e-3, weight_decay=0.0001)
    # Define the loss function for computing the training loss
    loss_fn = nn.CrossEntropyLoss()
    # Perform training for the specified number of epochs
    for epoch in range(num_epochs):
        print(f"Epoch {epoch + 1}\n-------------------------------")        
        # Train the model using the training data
        train(train_loader, model, optimizer, loss_fn)        
        # Evaluate the model on the test data
        test(test_loader, model, loss_fn)
    # Print a message indicating that the training is done
    print("Done!")
    # Save the trained model's state dictionary to a file
    torch.save(model.state_dict(), 'plants2.model')