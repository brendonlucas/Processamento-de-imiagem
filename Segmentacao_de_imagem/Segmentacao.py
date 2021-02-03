import cv2 as cv2
import numpy as np

def main():
    img = cv2.imread('Alcohol-Dehydrogenase.png')
    img = cv2.resize(img, (480, 550))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    item = 1
    nome = ''
    for i in range(4):
        if item == 1:
            # vermelho
            nome = "Parte vermelha"
            lower = np.array([0, 0, 0])
            upper = np.array([20, 255, 255])
            blur = cv2.medianBlur(hsv, 1)
        if item == 2:
            # verde
            nome = "Parte verde"
            lower = np.array([50, 1, 1])
            upper = np.array([114, 255, 255])
            blur = cv2.medianBlur(hsv, 1)
        if item == 3:
            # blue
            nome = "Parte azul"
            lower = np.array([74, 0, 60])
            upper = np.array([170, 255, 250])
            blur = cv2.medianBlur(hsv, 1)
        if item == 4:
            # amarelo
            nome = "Parte amarelo"
            lower = np.array([10, 0, 0])
            upper = np.array([50, 255, 255])
            blur = cv2.medianBlur(hsv, 1)

        mask = cv2.inRange(blur, lower, upper)
        res = cv2.bitwise_and(img, img, mask=mask)
        cv2.imshow(nome, res)

        item += 1

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
