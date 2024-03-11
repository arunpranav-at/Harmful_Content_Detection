
from PIL import Image 
from pytesseract import pytesseract 

def image_text_detection(image_path):
    # Definpiping paths to tesseract.exe 
    # and the image we would be using 
    # path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.paexe"
    path_to_tesseract = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
    
    # Opening the image & storing it in an image object 
    img = Image.open(image_path) 
    
    # Providing the tesseract executable 
    # location to pytesseract library 
    pytesseract.tesseract_cmd = path_to_tesseract 
    
    # Passing the image object to image_to_string() function 
    # This function will extract the text from the image 
    text = pytesseract.image_to_string(img) 
    
    # Displaying the extracted text 
    return text[:-1]

# if __name__ == "__main__":
#     main()