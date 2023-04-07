import cv2 as cv


def figure_detect(image: str):
    """
    Параметр image содержит путь до картинки
    :param image:
    :return:
    """
    img: str = cv.imread(image)
    cv.cvtColor(img, cv.COLOR_BRG2GRAY)
    cv.imshow('afs', img)
    cv.waitKey(0)


figure_detect(image='full.jpg')