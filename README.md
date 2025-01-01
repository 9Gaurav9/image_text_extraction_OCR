# Smart Image Text Extractor

**Smart Image Text Extractor** is a Python-based web application that uses Optical Character Recognition (OCR) to extract text from images. It provides an intuitive interface to upload images and retrieve the extracted text efficiently. The project supports both local and API-based OCR methods.

---

## Features
- **Image Upload**: Upload images directly from your browser.
- **Text Extraction**: Extracts text from uploaded images using OCR.
- **Preprocessing**: Includes grayscale conversion, noise reduction, and thresholding for better OCR accuracy.
- **Easy-to-Use UI**: A simple and interactive web interface built with JavaScript and Flask.
- **Multiple OCR Options**:
  - Local OCR using EasyOCR or Tesseract.
  - Cloud-based OCR using the OCR.space API.

---

## Prerequisites
1. Python 3.8+  
2. Required Libraries:
   - Flask
   - Flask-CORS
   - OpenCV
   - NumPy
   - EasyOCR or OCR.space API
3. [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) (optional if using EasyOCR or OCR.space).

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/smart-image-text-extractor.git
   cd smart-image-text-extractor
   ```

2. **Set Up Environment**:
   - Create a virtual environment (optional but recommended):
     ```bash
     python -m venv venv
     source venv/bin/activate  # For Linux/macOS
     venv\Scripts\activate     # For Windows
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Tesseract OCR** (optional for EasyOCR or OCR.space):
   - [Tesseract Installation Guide](https://github.com/UB-Mannheim/tesseract/wiki).

5. **Set Up OCR.space API Key** (if using OCR.space):
   - Sign up at [OCR.space](https://ocr.space/ocrapi) and get your API key.
   - Replace the placeholder `your_api_key_here` in `app.py` with your key.

---

## Usage

1. **Run the Application**:
   ```bash
   python app.py
   ```

2. **Access the Web Interface**:
   - Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

3. **Upload an Image**:
   - Click the "Upload" button, choose an image file, and wait for the extracted text to appear.

---

## Project Structure

```plaintext
smart-image-text-extractor/
├── app.py               # Backend application logic
├── templates/
│   └── index.html       # Frontend HTML template
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## Supported Image Formats
- `.jpg`
- `.jpeg`
- `.png`
- `.bmp`

---

## Future Enhancements
- Add support for batch image processing.
- Incorporate additional OCR languages.
- Provide options to download extracted text as a file.
- Integrate handwriting recognition.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

