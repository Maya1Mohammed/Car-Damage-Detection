import cv2 #image handling
import math #simplifying tasks like drawing styled bounding boxes and text on images.
import cvzone
from ultralytics import YOLO

yolo_model = YOLO("../Weights/best.pt")

#defining the classes (damaged areas) that the model was trained on
class_labels = ['Bodypanel-Dent', 'Front-Windscreen-Damage', 'Headlight-Damage', 
'Rear-windscreen-Damage', 'RunningBoard-Dent', 'Sidemirror-Damage', 'Signlight-Damage', 
'Taillight-Damage', 'bonnet-dent', 'boot-dent', 'doorouter-dent', 'fender-dent', 
'front-bumper-dent', 'pillar-dent', 'quaterpanel-dent', 'rear-bumper-dent', 'roof-dent']

image_path = 'Media/test/images/body_pannel--27-_jpg.rf.8ef259ab796cbe57783546913e7382de.jpg'
img = cv2.imread(image_path) #loads the image into a BGR format

#Object detection (predictions, bounding boxes, confidence score, class IDs)
results = yolo_model(img)

#For loop to draw bounding boxes over detected objects
for r in results:
    boxes = r.boxes
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0] #box coordinates (top left, bottom right)
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) #converting to int to draw rectangles with openCV

        w, h = x2 - x1, y2 - y1 #computing the width and height of the bounding box

        conf = math.ceil((box.conf[0] * 100 )) / 100 #confidence score of the bounding box
        cls = int(box.cls[0]) #class index (i.e., out-door)

        if conf > 0.3: #only draw detections if the confidence is > 30%
            cvzone.cornerRect(img, (x1, y1, w, h), t=2)
            cvzone.putTextRect(img, f'{class_labels[cls]} {conf}', (x1, y1 - 10), scale=0.8, thickness=1, colorR=(255,0,0))

#Display the image with detections
cv2.imshow("Image", img)

#Close window when 'q' button is pressed
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cv2.waitKey(1) 