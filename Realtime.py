#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pytesseract
from PIL import Image
import os,argparse
import cv2
import numpy as np


# In[ ]:


model = tf.keras.models.load_model('try.h5')
IMAGE_SIZE = 200
def tests(img):
    img = cv2.resize(img,(IMAGE_SIZE,IMAGE_SIZE))
    img = img / 255
    img = np.reshape(img,(1,IMAGE_SIZE,IMAGE_SIZE,3))
    y = model.predict(img)
    y = y*255
    img = np.reshape(img,(IMAGE_SIZE,IMAGE_SIZE,3))
    a = [int(x) for x in y[0]]
    print(y)
    print(a)
    arr=[a[2],a[3],a[0],a[3],a[0],a[1],a[2],a[1]]
    #print(ac,bc,cc,dc)
    image = cv2.rectangle(img,(int(y[0][0]),int(y[0][1])),(int(y[0][2]),int(y[0][3])),(0, 0, 255))
#     plt.imshow(image)
#     plt.show()
    return image,arr


# In[5]:


cap = cv2.VideoCapture(0)
while True:
    success,img = cap.read()
    #img=Plate(img)
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img2,array=tests(gray)
    a=(array[0],array[1])
    b=(array[2],array[3])
    c=(array[4],array[5])
    d=(array[6],array[7])
    crop=img2[a[1]:c[1],a[0]:c[0]]
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    filename = "fin.png".format(os.getpid())
    cv2.imwrite(filename, crop)
    text = pytesseract.image_to_string(Image.open(filename))
    os.remove(filename)
    print(text)
    cv2.imshow("Output",img)
    k=cv2.waitKey(1)
    if k%256==27:
        print('closing app')
        break
cap.release()
cv2.destroyAllWindows() 
    


# In[ ]:




