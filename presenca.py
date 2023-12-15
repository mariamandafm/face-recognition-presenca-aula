import cv2
from datetime import datetime
from Adafruit_IO import Client, Feed
from base64 import b64encode

from reconhecer_rostos import aferir_presenca

alunos = {
    "jim_helpert": "Jim Helpert",
    "michael_scott": "Michael Scott",
    "dwight_schrute": "Dwight Schrute",
    "pam_beesly": "Pam Beesly",
    "ryan_howard": "Ryan Howard",
    "andy_bernard": "Andy Bernard",
    "kevin_malone": "Kevin Malone",
    "angela_martin": "Angela Martin",
    "kelly_kapoor": "Kelly Kapoor",
    "oscar_martinez": "Oscar Martinez",
    "Unknown": "Desconhecido"
}

# Function to capture an image
def capture_image():
    # Access the default camera (index 0)
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the captured frame
        cv2.imshow('Press "p" to capture', frame)

        # Wait for 'p' key to be pressed
        if cv2.waitKey(1) & 0xFF == ord('p'):
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

            # Construct the file name with the current date and time
            file_name = f"captured_image_{current_time}.jpg"

            # Save the captured image with the constructed file name
            cv2.imwrite(file_name, frame)
            print("Image captured!")
            break

    # Release the camera and close the OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function to capture an image
# capture_image()


presentes = aferir_presenca('reuniao/ex1.png')
if (len(presentes) > 0):
    print("Presentes: ")
    for presente in presentes:
        print(alunos[presente])

quantidade_presentes = len(presentes)

clientREST = Client(username='XX', key='XX')

feed = Feed(name='presenca')

clientREST.send_data('presenca', quantidade_presentes)

