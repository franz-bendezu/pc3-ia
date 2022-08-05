
import os
import cv2


def read_image(index):
    tagged_folder = "./data/tagged/"
    source = tagged_folder + str(index) + ".jpg"
    filename = f"{source}"
    img = cv2.imread(filename, 0)
    cv2.imshow('img  ', img)
    cv2.waitKey(33)
    name = input('What is name?\n')
    if(len(name) != 5):
        return
    template_target_path = tagged_folder + str(name) + "_000%s" + ".jpg"
    id = 1
    while os.path.exists(template_target_path % id):
        id += 1
    target_path = template_target_path % id
    print(target_path)
    os.rename(source, target_path)


for i in range(364, 975):
    print(i)
    read_image(i)
