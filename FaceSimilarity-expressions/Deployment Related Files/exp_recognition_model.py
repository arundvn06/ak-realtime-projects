import torch
import torchvision
import torch.nn as nn
from torchvision import transforms
## Add more imports if required

####################################################################################################################
# Define your model and transform and all necessary helper functions here                                          #
# They will be imported to the exp_recognition.py file                                                             #
####################################################################################################################

# Definition of classes as dictionary
classes = {0: 'ANGER', 1: 'DISGUST', 2: 'FEAR', 3: 'HAPPINESS', 4: 'NEUTRAL', 5: 'SADNESS', 6: 'SURPRISE'}

# Example Network
class facExpRec(torch.nn.Module):
    def __init__(self):
        #YOUR CODE HERE
        
    def forward(self, x):
        #YOUR CODE HERE
        
# Sample Helper function
def rgb2gray(image):
    return image.convert('L')
    
# Sample Transformation function
#YOUR CODE HERE for changing the Transformation values.
trnscm = transforms.Compose([rgb2gray, transforms.Resize((48,48)), transforms.ToTensor()])