import cv2
import os


video=cv2.VideoCapture(0)

# para fazer a leitura dos rostos
facedetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

count=0

nameID=str(input("Digite o nome: ")).lower()

path='images/'+nameID

isExist = os.path.exists(path)

if isExist:
	print("Pasta com o nome já existe")
	nameID=str(input("Digite o nome novamente: "))
else:
	os.makedirs(path)

while True:
	ret,frame = video.read()
	faces=facedetect.detectMultiScale(frame,1.3, 5)  # comentar para video, descomentar para detecção
	for x,y,w,h in faces:  # comentar para video, descomentar para detecção
		count=count+1
		name='./images/'+nameID+'/'+ str(count) + '.jpg'
		print("Creating Images........." +name)
		cv2.imwrite(name, frame[y:y+h,x:x+w])
		cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)  # comentar para video, descomentar para detecção
	cv2.imshow("WindowFrame", frame)
	cv2.waitKey(1)
	if count>450:  # if k == ord('q'):
		break
video.release()
cv2.destroyAllWindows()