import cv2 
import os 
from PIL import Image
import pytesseract
import re
import pandas as pd

# Include tesseract executable in your path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
  
# Read the video from specified path 
cam = cv2.VideoCapture("C:\\Users\\YASH\\Desktop\\Image Test Cases\\smallvideo_test.mp4") 

try: 
      
    # creating a folder named data 
    if not os.path.exists('Desktop\data'): 
        os.makedirs('data') 
  
# if not created then raise error 
except OSError: 
    print ('Error: Creating directory of data') 
  
# frame 
currentframe = 0
  
while(True): 
      
    # reading from frame 
    ret,frame = cam.read() 
  
    if ret: 
        # if video is still left continue creating images 
        name = './data/frame' + str(currentframe) + '.jpg'
        print ('Creating...' + name) 
        # writing the extracted images 
        cv2.imwrite(name, frame) 
  
        # increasing counter so that it will 
        # show how many frames are created 
        currentframe += 1
    else: 
        break
  
# Release all space and windows once done 
cam.release() 
cv2.destroyAllWindows() 

  
f = []
t = []
input_dir = r'C:/Users/YASH/data/'

for root, dirs, filenames in os.walk(input_dir):
    for filename in filenames:
        try:
            print(filename)
            f.append(filename)
            img = Image.open(input_dir+ filename)
            text = pytesseract.image_to_string(img, lang = 'eng')
            t.append(text)
            print(text)
            print('-='*20)
        except:
            continue


#df = pd.DataFrame(list(zip(f, t)),columns=['file_Name','Text'])