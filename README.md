# 🧠 Intel Image Classifier

An end-to-end Deep Learning web application that classifies natural scene images into six categories using a Convolutional Neural Network (CNN) built with PyTorch.

## 🚀 Features

- Upload an image through a web interface.
- Predict one of six scene categories.
- Display prediction confidence.
- FastAPI backend for inference.
- HTML, CSS and JavaScript frontend.
- Dockerized for easy deployment.

## 📂 Project Structure

```
Intel_Image_Classifier/
│
├── app.py
├── model.py
├── class_names.py
├── cnn_intel.pth
├── requirements.txt
├── Dockerfile
│
├── static/
│   ├── index.html
│   ├── style.css
│   └── script.js
```

## 🛠 Technologies

- Python
- PyTorch
- Torchvision
- FastAPI
- HTML
- CSS
- JavaScript
- Docker
- Git
- GitHub

## 🧠 Model

The CNN model consists of:

- 2 Convolution Layers
- ReLU Activation
- MaxPooling
- Fully Connected Layers
- Softmax for prediction probabilities

Input Size:

```
150 × 150 × 3
```

Output Classes:

- Buildings
- Forest
- Glacier
- Mountain
- Sea
- Street

## 📊 Performance

Test Accuracy:

```
77.87%
```

## 🖥 Running Locally

Install dependencies

```bash
pip install -r requirements.txt
```

Run the API

```bash
uvicorn app:app --reload
```

Open

```
http://127.0.0.1:8000
```

## 🐳 Docker

Build

```bash
docker build -t intel-classifier .
```

Run

```bash
docker run -p 8000:8000 intel-classifier
```

## 📸 Demo

(Add screenshots here)

---

Created by **Youssef Yasser**
