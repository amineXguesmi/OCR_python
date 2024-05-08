### 🔍 OCR M-Service

- **Functionality**: Extracts information from uploaded documents.
- **Integration**: Utilized by the Commercial and Risk Management Services to process financial documents.

## 📋 Requirements

1. Download Tesseract executable from [here](https://github.com/UB-Mannheim/tesseract/wiki).
2. Install the executable in `C:\Program Files (x86)\Tesseract-OCR`.
3. Add Tesseract OCR to your environment variables:
   - `PATH`: `C:\Program Files\Tesseract-OCR`
   - `TESSDATA_PREFIX`: `C:\Program Files\Tesseract-OCR\tessdata`
4. Run `pip install pytesseract`.
5. Run `python ocr.py`.

