import cv2

img = cv2.imread("road1.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

stop_data = cv2.CascadeClassifier("haarcascade_stopsign.xml")
stop_coords = []

try:
    stop_coords = stop_data.detectMultiScale(img_gray, minSize=(20, 20)).tolist()
except:
    print("stop sign not found")

def check_forward(stop_coords):
    if len(stop_coords) != 0:
        return False
    else:
        return True

print("u can move:", check_forward(stop_coords))
