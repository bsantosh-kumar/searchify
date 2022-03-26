
from matplotlib.pyplot import get


def tesseract_ocr(file_name,lang='eng'):
    """
    This function will read the given file in parameter and return the text
    extracted from the image using tesseract.
    """
    from subprocess import Popen, PIPE
    from PIL import Image
    import pytesseract
    import os
    import cv2
    import numpy as np

    file_name = os.path.join(os.path.dirname(__file__), file_name)
    assert os.path.exists(file_name)
    # Read image using opencv
    img = cv2.imread(file_name)

    # Convert to gray
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # # Apply dilation and erosion to remove some noise
    # kernel = np.ones((1, 1), np.uint8)
    # img = cv2.dilate(img, kernel, iterations=1)
    # img = cv2.erode(img, kernel, iterations=1)

    # # Write image after removed noise
    # cv2.imwrite("removed_noise.png", img)

    # #  Apply threshold to get image with only black and white
    # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite("thres.png", img)
    pytesseract.pytesseract.tesseract_cmd = r'C://Users//Rahul//Desktop//Codes//practice//test//Tessaract-ocr//tesseract.exe'
    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open("thres.png"), lang=lang)

    # # # Remove template file
    # os.remove("removed_noise.png")
    # os.remove("thres.png")

    return result

def split_string(txt) :
    import re
    txt = txt.lower()
    txt = re.sub(r'[^\w\s]',' ',txt)
    txt = re.sub(r'\s+',' ',txt)
    return txt.split()

def get_words(file) :
    text = tesseract_ocr(file)
    return split_string(text)


print(get_words("test.jpg"))
print(get_words("test1.jpeg"))
print(get_words("test2.jpeg"))
print(get_words("test3.jpeg"))
