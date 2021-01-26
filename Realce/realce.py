import cv2 as cv2
import numpy as np


def main():
    img = cv2.imread('image.jpg', 1)
    img = cv2.resize(img, (480, 550))

    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    img_negative = cv2.bitwise_not(img_gray)
    img_contra = cv2.convertScaleAbs(img_gray, alpha=2.0, beta=50)
    img_gamma = adjust_gamma(img_gray, 2.0)
    img_log = adjust_log(img_gray)

    cv2.imshow('Negative', img_negative)
    cv2.imshow('Contrast', img_contra)
    cv2.imshow('Gamma', img_gamma)
    cv2.imshow('Log', img_log)

    cv2.imwrite("Negative.png", img_negative)
    cv2.imwrite("Contrast.png", img_contra)
    cv2.imwrite("Gama.png", img_gamma)
    cv2.imwrite("log.png", img_log)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def adjust_gamma(image, gamma):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255
                      for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)


def adjust_log(image):
    c = 255 / np.log(1 + np.max(image))
    log_image = c * (np.log(image + 1))
    return np.array(log_image, dtype=np.uint8)


if __name__ == '__main__':
    main()
