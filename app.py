from fastapi import FastAPI, UploadFile, File
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

import torch
from torchvision import transforms
from PIL import Image

from model import CNN
from class_names import CLASS_NAMES


app = FastAPI(
    title="Intel Image Classifier API",
    description="CNN Model for Intel Image Classification",
    version="1.0.0"
)

# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")


# ================= MODEL ================= #

model = CNN()

model.load_state_dict(
    torch.load("cnn_intel.pth", map_location="cpu")
)

model.eval()

transform = transforms.Compose([
    transforms.Resize((150, 150)),
    transforms.ToTensor()
])


# ================= HOME PAGE ================= #

@app.get("/")
def home():
    return FileResponse("static/index.html")


# ================= PREDICT ================= #

@app.post("/predict")
def predict(file: UploadFile = File(...)):

    image = Image.open(file.file).convert("RGB")

    image = transform(image)

    image = image.unsqueeze(0)

    with torch.no_grad():

        outputs = model(image)

        probabilities = torch.softmax(outputs, dim=1)

        predicted = torch.argmax(probabilities, dim=1)

        confidence = probabilities[0][predicted.item()] * 100

        prediction = CLASS_NAMES[predicted.item()]

        if confidence.item() < 60:
            prediction = "Unknown"

    return {
        "prediction": prediction,
        "confidence": round(confidence.item(), 2)
    }