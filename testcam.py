import cv2

# เปิดกล้องเว็บแคม
cap = cv2.VideoCapture(0)

# ตรวจสอบว่ากล้องเปิดสำเร็จหรือไม่
if not cap.isOpened():
    print("ไม่สามารถเปิดกล้องเว็บแคมได้")
    exit()

# ตั้งค่าขนาดที่ต้องการ
width = 640
height = 480

while True:
    # อ่านเฟรมจากกล้องเว็บแคม
    ret, frame = cap.read()
    
    # ตรวจสอบว่าเฟรมถูกอ่านสำเร็จหรือไม่
    if not ret:
        print("ไม่สามารถอ่านเฟรมจากกล้องได้")
        break
    
    # ปรับขนาดเฟรม
    resized_frame = cv2.resize(frame, (width, height))
    
    # แสดงเฟรม
    cv2.imshow('Webcam', resized_frame)
    
    # รอการกดปุ่ม 'q' เพื่อออกจากลูป
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ปิดกล้องเว็บแคมและปล่อยทรัพยากร
cap.release()
cv2.destroyAllWindows()
