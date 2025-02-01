import torch
from PIL import Image
from torchvision import transforms

# Load the pretrained ResNet model
image_model = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True)
image_model.eval()

# Image preprocessing
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def classify_image(image_path):
    image = Image.open(image_path).convert("RGB")
    input_tensor = preprocess(image).unsqueeze(0)
    with torch.no_grad():
        output = image_model(input_tensor)
    probabilities = torch.nn.functional.softmax(output[0], dim=0)
    top5_prob, top5_catid = torch.topk(probabilities, 5)
    return [(f"Class {i.item()}", f"{p.item():.2%}") for p, i in zip(top5_prob, top5_catid)]
