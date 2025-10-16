try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

# Add the following line if Tesseract is not in your PATH.
# You may need to change the path depending on where you install it.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))
    return text

print(ocr_core('one.png'))
