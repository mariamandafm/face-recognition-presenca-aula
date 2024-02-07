import cv2
from datetime import datetime
from Adafruit_IO import Client, Feed

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
    "oscar_martinez": "Oscar Martinez"
}

def capture_image():
    video_file_path = 'reuniao/meeting.mp4'
    cap = cv2.VideoCapture(video_file_path)

    while True:
        ret, frame = cap.read()

        cv2.imshow('Press "p" to capture', frame)

        if cv2.waitKey(33) & 0xFF == ord('p'):
            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

            file_name = f"reuniao/captured_image_{current_time}.jpg"

            cv2.imwrite(file_name, frame)
            break

    cap.release()
    cv2.destroyAllWindows()
    return file_name


imagem = capture_image()
presentes = aferir_presenca(imagem)


def criar_texto(pessoas):
    texto = ''
    if (len(pessoas) > 0):
        for aluno in pessoas:
            texto += alunos[aluno] + '\n'
    return texto


faltas = list(set(alunos.keys()) - presentes)

quantidade_presentes = len(presentes)
alunos_presentes = criar_texto(presentes)
alunos_falta = criar_texto(faltas)

clientREST = Client(username='mariamanda', key='aio_LqTD90xkOTBf8jWwStUF78gUZhZE')
feed = Feed(name='presenca')

clientREST.send_data('presenca', quantidade_presentes)

if (alunos_presentes):
    clientREST.send_data('alunos', alunos_presentes)
else:
    clientREST.send_data('alunos', "Nenhum aluno está presente")

if (alunos_falta):
    clientREST.send_data('faltas', alunos_falta)
else:
    clientREST.send_data('alunos', "Todos estão presente")
