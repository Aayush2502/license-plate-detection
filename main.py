import cv2
import pytesseract
import keyboard

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

##################################################################################
frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier(cv2.haarcascades + "haarcascade_russian_plate_number.xml")
minArea = 500
states = ['AN', 'AP', 'AR', 'AS', 'BR', 'CH', 'DN', 'DD', 'DL', 'GA', 'GJ', 'HR', 'JK', 'KA', 'KL', 'LD',
          'MP', 'MH', 'MN', 'ML', 'MZ', 'NL', 'OD', 'PY', 'PN', 'RJ', 'SK', 'TN', 'TR', 'UP', 'WB', 'CG',
          'TS', 'JH', 'UK']
#################################################################################
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)
count = 0
plates = []
correct = []

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w * h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (51, 51, 255), 2)

            imgRoi = img[y:y + h, x:x + w]
            #cv2.imshow("Detected Plate", imgRoi)
            read = pytesseract.image_to_string(imgRoi)
            read = ''.join(e for e in read if e.isalnum())
            if read != '':
                print(read)
                plates.append(read)
            cv2.rectangle(img, (x, y), (x + w, y + h), (51, 51, 255), 2)
            #cv2.rectangle(img, (x, y - 40), (x + w, y), (51, 51, 255), -1)
            #cv2.putText(img, read, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("./scan/noPlate_" + str(count) + ".jpg", imgRoi)
        cv2.imwrite('./img/result.jpg', imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "scan saved", (150, 255), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255), 2)
        cv2.imshow("Camera", img)
        cv2.waitKey(50)
        count += 1
    if keyboard.is_pressed('e'):
        cv2.destroyAllWindows()
        break
print("Plates:", plates)
for i in plates:
    if len(i) == 10:
        if i[0:2] in states:
            correct.append(i)
correct = set(correct)
print('Correct:', correct)
f = open("./scan/Correct plates.txt", 'w')
for i in correct:
    f.write(i)
    f.write('\n')
