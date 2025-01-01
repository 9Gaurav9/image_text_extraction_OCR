from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import cv2
import easyocr
import numpy as np

app = Flask(__name__)
CORS(app)  # Enable CORS to allow frontend-backend communication

# Create an EasyOCR reader instance
reader = easyocr.Reader(['en'])

# Serve the HTML file
@app.route('/')
def index():
    return send_from_directory('', 'index.html')

# OCR endpoint
@app.route('/extract-text', methods=['POST'])
def extract_text():
    if 'image' not in request.files:
        return jsonify({"error": "No image provided"}), 400
    
    file = request.files['image']
    try:
        # Read image
        image = np.frombuffer(file.read(), np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        if image is None:
            return jsonify({"error": "Invalid image format"}), 400

        # Pre-process the image (same as before)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
        _, threshold_image = cv2.threshold(blurred_image, 128, 255, cv2.THRESH_BINARY)

        # Perform OCR with EasyOCR
        result = reader.readtext(threshold_image)
        text = " ".join([text[1] for text in result])

        return jsonify({"text": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
