import cv2
import os

cam = cv2.VideoCapture(0)

cam.set(3,640)
cam.set(4,480)

face_detector = cv2.CascadeClassifier('Cascades\haarcascade_frontalface_default.xml')
path = "Program Face Recognition (IoT)"

face_id = input('\n Masukkan ID Gambar : ')
print("\n Silahkan Lihat ke Arah Webcam...")

if not os.path.exists('dataset'):
    os.makedirs('dataset')

count = 0

while(True):
    ret, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 2)
        count+=1
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) +".jpg", gray[y:y+h, x:x+w])      #function buat save gambar dengan format .jpg dalam bentuk gray
        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff

    if k == 27:
        break
    elif count>=100:
        break

print("\n Pengambilan Dataset Telah Selesai...")

cam.release()
cv2.destroyAllWindows()
