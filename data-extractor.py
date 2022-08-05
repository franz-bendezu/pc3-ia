import calendar
from datetime import datetime
import os
import requests
import pytesseract
import cv2
import json
from PIL import Image
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
IMAGE_URL = "http://apps2.mef.gob.pe/consulta-vfp-webapp/Captcha.jpg"


characters = "123456789abcdefghijklmnpqrstuvwxyz"
captcha = ""


def add_tagged_image(img, name):
    template_source_path = "./data/tagged/" + str(name) + "_000%s" + ".jpg"
    id = 1
    while os.path.exists(template_source_path % id):
        id += 1
    source_path = template_source_path % id
    print(source_path)
    cv2.imwrite(source_path, img)


def get_captcha(img):
    captcha = pytesseract.image_to_string(
    img, config='--psm 8 -c tessedit_char_whitelist=0123456789abcdefghijkmnlopqrsturstuvwxyz')
    captcha = captcha.replace(" ", "").strip()
    return captcha


def read_image(index):
    source = "./data/original/" + str(index) + ".jpg"
    filename = f"{source}"
    origin_img = cv2.imread(filename, 0)
    img = cv2.imread(filename, 0)
    thresh  = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    kernel = np.ones((2,2),np.uint8)    
    closing   = cv2.morphologyEx(thresh, cv2.MORPH_GRADIENT, kernel)

    horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 1))
    detected_lines = cv2.morphologyEx(
    thresh, cv2.MORPH_OPEN, horizontal_kernel, iterations=2)
    cnts = cv2.findContours(
        detected_lines, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    for c in cnts:
        cv2.drawContours(img, [c], -1, (255, 255, 255), 2)

    # Repair image
    repair_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,6))
    result = 255 - cv2.morphologyEx(255 - img, cv2.MORPH_CLOSE, repair_kernel, iterations=1)

    cv2.imshow('closing  ', closing  )
    cv2.imshow('thresh', thresh)
    cv2.imshow('detected_lines', detected_lines)
    cv2.imshow('image', img)
    cv2.imshow('result', result)
    cv2.waitKey()

    print(get_captcha(kernel))


for i in range(1000):
    print(i)
    read_image(i)


def download_image(index):
    img_data = requests.get(IMAGE_URL).content
    route = "./data/original/" + str(index) + ".jpg"
    with open(route, 'wb') as handler:
        handler.write(img_data)
