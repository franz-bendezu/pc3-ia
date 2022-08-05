from ast import Str
import cv2
import numpy as np


def add_proccesed_image(img, name):
    source_path = "./data/process/" + str(name) + ".jpg"
    cv2.imwrite(source_path, img)


def process_image(img, thresh):
    [contours, hierarchy] = cv2.findContours(
        thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    mask = np.zeros(img.shape, np.uint8)
    largest_areas = sorted(contours, key=cv2.contourArea)
    cv2.drawContours(mask, [largest_areas[-2]], 0, (255, 255, 255, 255), -1)
    removed = cv2.add(thresh, mask)

    [contours, hierarchy] = cv2.findContours(
        thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)

    contours = cv2.drawContours(thresh, contours, 0, (255, 50, 50), -1)

    kernel = np.ones((3, 3), np.uint8)
    morph = cv2.morphologyEx(contours, cv2.MORPH_OPEN, kernel)

    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(morph, kernel, iterations=1)
    img2 = morph - (erosion)
    result = thresh-img2

def read_image(index):
    source = "./data/original/" + str(index) + ".jpg"
    filename = f"{source}"
    img = cv2.imread(filename, 0)
    thresh = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


    add_proccesed_image(thresh, str(index)+'-thresh')
    source = "./data/process/" + str(index)+'-thresh' + ".jpg"
    filename = f"{source}"
    img = cv2.imread(filename, 0)
   # findcontours
    image_contours = np.zeros((img.shape[1], img.shape[0], 1), np.uint8)

    image_binary = np.zeros((img.shape[1], img.shape[0], 1), np.uint8)

    print(img.shape[1])

    for channel in range(img.shape[1]):
        ret, image_thresh = cv2.threshold(img[:, :, channel], 127, 255, cv2.THRESH_BINARY)    
        contours = cv2.findContours(image_thresh, 1, 1)[0]   
        cv2.drawContours(image_contours, contours, -1, (255,255,255), 3)

    contours = cv2.findContours(image_contours, cv2.RETR_LIST,
                            cv2.CHAIN_APPROX_SIMPLE)[0]

    cv2.drawContours(image_binary, [max(contours, key = cv2.contourArea)],
                    -1, (255, 255, 255), -1)


    cv2.imshow("image_binary", image_binary)
    cv2.imshow("Img", img)
    cv2.waitKey(0)
    add_proccesed_image(img, index)


for i in range(1000):
    print(i)
    read_image(i)
