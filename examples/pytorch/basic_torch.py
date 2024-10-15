import torch
import torch.nn as nn

# Define a simple neural network
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(10, 5)
        self.fc2 = nn.Linear(5, 1)

    def forward(self, x):
        x = self.fc1(x)
        x = torch.relu(x)
        x = self.fc2(x)
        return x

# Create an instance of the network
net = Net()

# Create some input data
input_data = torch.randn(1, 10)

# Pass the input data through the network
output = net(input_data)

# Print the output
print(output)
