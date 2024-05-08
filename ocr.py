from flask import Flask, request, jsonify
from PIL import Image

import pytesseract

app = Flask(__name__)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/ocr', methods=['POST'])
def ocr():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    
    if file.filename == '' or not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        return jsonify({'error': 'Invalid file format, must be PNG or JPEG'}), 400
    
    image = Image.open(file)
    
    extracted_text = pytesseract.image_to_string(image)
    
    return jsonify({'text': extracted_text}), 200

if __name__ == '__main__':
    app.run(debug=True)