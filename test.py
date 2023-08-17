import pytesseract
print(pytesseract.image_to_string(image='sample.pdf'))
print('hello')

pytesseract.pytesseract.tesseract_cmd=r'C:\Users\P2848116\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

#C:\Users\P2848116\AppData\Local\Programs\Tesseract-OCR