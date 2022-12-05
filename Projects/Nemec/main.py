import cv2

cap = cv2.VideoCapture("Example_video.mp4")

object_detector = cv2.createBackgroundSubtractorMOG2(history = 50 , varThreshold=60)

while True:
    ret, frame = cap.read()

    #Extract region of interest:
    roi = frame[80:580, 60:275]

    #Oject Detection
    mask = object_detector.apply(roi)
    _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_KCOS)

 
    for cnt in contours:
        # Calculate area and remove small elements:
        area = cv2.contourArea(cnt)
        if area > 300:
            cv2.drawContours(roi, [cnt], -1, (0,255,0), 2)
            #x,y,w,h = cv2.boundingRect(cnt)
            #cv2.rectangle(roi, (x,y),(x+w,y+h), (0,255,0),2)
 
    cv2.imshow("Frame", frame)
    cv2.imshow("roi", roi)


    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()