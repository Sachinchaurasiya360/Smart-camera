import cv2
cap = cv2.VideoCapture(0);
print(cv2.CAP_PROP_FRAME_WIDTH) 
print(cv2.CAP_PROP_FRAME_HEIGHT)
while True:
    ret,frame=cap.read()
    name=cv2.putText(frame,'Hello World',(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow('name',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()