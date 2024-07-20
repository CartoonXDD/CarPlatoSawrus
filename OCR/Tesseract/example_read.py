import pytesseract
from PIL import Image
import time

pytesseract.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR/tesseract.exe"

image_path = 'tsrgt/1.jpg'

image = Image.open(image_path).convert('L')# L = gray, 1 = binarize
print(image.size)
t = time.time()
text = pytesseract.image_to_string(image, lang='tha').replace(' ', '') # lang = {}.traineddata
print("\n\n\n")
print(time.time()-t)

print(text)
