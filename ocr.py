from PIL import Image
import pytesseract
from config import SCREENSHOT_PATH, TESSERACT_PATH

# Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def extract_text_from_image():
    """Uses Tesseract OCR to extract text from the screenshot."""
    image = Image.open(SCREENSHOT_PATH)
    text = pytesseract.image_to_string(image)
    return text.strip()
