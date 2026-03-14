import cv2

img = cv2.imread('road2.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

car_data = cv2.CascadeClassifier('haarcascade_cars.xml')
stop_data = cv2.CascadeClassifier('haarcascade_stopsign.xml')

stop_coords = []
car_coords = []

try:
    car_coords = car_data.detectMultiScale(img_gray, minSize=(20, 20)).tolist()
    print(car_coords)
except:
    print('Car is NOT founded')

try:
    stop_coords = stop_data.detectMultiScale(img_gray, minSize=(20, 20)).tolist()
except:
    print('Znaki STOP ne naides')

def check_forward(car_coords, stop_coords):
    if len(stop_coords) != 0:
        return False
    elif len(car_coords) == 0:
        return True
    else:
        for (x, y, width, height) in car_coords:
            if width / img_width > 0.15:
                return False
        return True

img_height, img_width, img_channels = img.shape

print(check_forward(car_coords, stop_coords))