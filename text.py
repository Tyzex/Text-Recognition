import pytesseract
import cv2 as cv


class ExtractText(object):
    def __init__(self, path):
        self.path = path

    def gettext(self):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        filepath = self.path
        image = cv.imread(filepath)
        image = cv.resize(image, (300, 300))
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        addimage = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 81, 9)
        text = pytesseract.image_to_string(addimage)
        return text
