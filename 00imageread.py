import cv2
img_file = "./img/girl.jpg"
img = cv2.imread(img_file)
cv2.imshow("IMG", img)
cv2.waitKey() # 키가 입력될 때까지 대기
cv2.destroyAllWindows() # 창 모두 닫기

from PIL import Image
img = Image.open("./img/girl.jpg")
img.show()