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
<img width="651" height="762" alt="Screenshot 2026-07-04 084849" src="https://github.com/user-attachments/assets/d34fd609-7ff9-445e-b923-4bd7ab552321" />

<img width="647" height="826" alt="Screenshot 2026-07-04 084908" src="https://github.com/user-attachments/assets/39f50c5a-7cdb-4c49-a2af-4194ee8cf535" />

<img width="1433" height="267" alt="Screenshot 2026-07-04 084246" src="https://github.com/user-attachments/assets/41c1b506-7aa1-4a3a-8992-295a850bf19a" />

<img width="1825" height="821" alt="Screenshot 2026-07-04 084141" src="https://github.com/user-attachments/assets/8452187d-6bd7-4c63-b87c-d6485ad69420" />

<img width="518" height="817" alt="Screenshot 2026-07-04 083706" src="https://github.com/user-attachments/assets/a1f517d0-dffd-446f-a586-bf114a9dfab0" />






---

Created by **Youssef Yasser**
