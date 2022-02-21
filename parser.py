import pytesseract
import cv2
def recognision(address: str) -> None: 
    """
    requires:
    $ sudo apt install tesseract-ocr (ubuntu, idk bout arch/manjaro)
    $ sudo apt-get install tesseract-ocr-ukr (ubuntu, idk bout arch/manjaro)
    $ pip install opencv-contrib-python
    $ pip install pytesseract

    Parses the text without precision
    Param: address: str -- string of address of photo without .jpeg and folder name. 
    """
    image= cv2.imread('photos/'+address+'.jpeg')
    text = pytesseract.image_to_string(image, lang='ukr')
    with open ('text_files/'+address+'.txt', mode = 'w', encoding='utf-8')as file:
        file.write(text)

# recognision('Lopatin_Z_02_O')