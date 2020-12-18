import cv2
def openph(var):
    x= var.get()
    y = str(x) + '.jpg'
    cv2.namedWindow(y,cv2.WINDOW_GUI_NORMAL)
    img = cv2.imread(y)
    cv2.imshow(y, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()