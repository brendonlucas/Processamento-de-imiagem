import cv2 as cv2

def main():
    img = cv2.imread('image.jpg', 1)
    img = cv2.resize(img, (480, 550))

    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    img_media = cv2.blur(img_gray, (5, 5))
    img_mediana = cv2.medianBlur(img_gray, 5)
    img_gaussiano = cv2.GaussianBlur(img_gray, (5, 5), 0)

    cv2.imwrite("Media.png", img_media)
    cv2.imwrite("Mediana.png", img_mediana)
    cv2.imwrite("Gaussiano.png", img_gaussiano)

    cv2.imshow('Media', img_media)
    cv2.imshow('Mediana', img_mediana)
    cv2.imshow('Gaussiano', img_gaussiano)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()