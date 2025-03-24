const webcamElement = document.getElementById("webcam");
const canvasElement = document.getElementById("canvas");
const snapButton = document.getElementById("snap");
const uploadInput = document.getElementById("upload");
const loadingIndicator = document.getElementById("loading");

const webcam = new Webcam(webcamElement, "user", canvasElement, null);

function startWebcam() {
    webcam.start()
        .then(() => {
            console.log("Webcam started successfully");
            webcamElement.style.display = "block";
            canvasElement.style.display = "none";
            loadingIndicator.style.display = "none";
        })
        .catch(err => {
            console.error("Error starting webcam:", err);
            alert("Please allow camera access and refresh the page.");
        });
}
startWebcam();

// Function to display the captured/uploaded image
function displayImage(imageSrc){
    webcamElement.style.display = "none";
    canvasElement.style.display = "block";

    const ctx = canvasElement.getContext("2d");
    const img = new Image();
    img.onload = function () {
        // Set the canvas size to 400x400
        canvasElement.width = 400;
        canvasElement.height = 400;

        // Draw image scaled to fit 400x400
        ctx.drawImage(img, 0, 0, 400, 400);
    };
    img.src = imageSrc;
}


// Function to handle image processing and API call
function processImage(imageSrc) {
    loadingIndicator.textContent = "Processing...";
    loadingIndicator.style.display = "block";

    // Convert to Blob and send API request
    canvasElement.toBlob(blob => {
        let formData = new FormData();
        formData.append("image", blob, "snapshot.jpg");

        fetch("/upload/", {
            method: "POST",
            body: formData
        })
            .then(response => response.blob())
            .then(blob => {
                let audioUrl = URL.createObjectURL(blob);
                let audio = new Audio(audioUrl);
                audio.play();
            })
            .catch(error => console.error("Error:", error))
            .finally(() => {
                // Restart camera after processing
                startWebcam();
            });
    }, "image/png");
}

// Snap button event (Capture from webcam)
snapButton.addEventListener("click", () => {
    let picture = webcam.snap();
    displayImage(picture);
    processImage(picture);
});

// Upload button event (Upload from file)
uploadInput.addEventListener("change", (event) => {
    const file = event.target.files[0];

    if (file && file.type.startsWith("image/")) {
        const reader = new FileReader();
        reader.onload = function (e) {
            displayImage(e.target.result)
            processImage(e.target.result);
        };
        reader.readAsDataURL(file);
    } else {
        alert("Please upload a valid image file.");
    }
});
