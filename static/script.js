const imageInput = document.getElementById("imageInput");

const preview = document.getElementById("preview");

const predictBtn = document.getElementById("predictBtn");

const prediction = document.getElementById("prediction");

const confidence = document.getElementById("confidence");


// =====================
// Preview Image
// =====================

imageInput.addEventListener("change", function () {

    const file = imageInput.files[0];

    if (!file) return;

    preview.src = URL.createObjectURL(file);

    preview.style.display = "block";

});


// =====================
// Predict
// =====================

predictBtn.addEventListener("click", async function () {

    const file = imageInput.files[0];

    if (!file) {

        alert("Please choose an image first!");

        return;
    }

    const formData = new FormData();

    formData.append("file", file);

    prediction.innerHTML = "Predicting...";

    confidence.innerHTML = "";

    const response = await fetch("/predict", {

        method: "POST",

        body: formData

    });

    const result = await response.json();

    prediction.innerHTML = "Prediction: " + result.prediction;

    confidence.innerHTML = "Confidence: " + result.confidence + "%";

});