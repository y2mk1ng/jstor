import pytesseract
import PIL
from PIL import Image

text = pytesseract.image_to_string(Image.open('origin.png'))
print(text)
