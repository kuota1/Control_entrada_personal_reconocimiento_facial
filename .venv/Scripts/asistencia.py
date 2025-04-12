import cv2  
import face_recognition as fr
import os
import numpy as np
from datetime import datetime
import dlib

# Cargar el detector y el predictor de landmarks de ojos
predictor_path = "shape_predictor_68_face_landmarks.dat"
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

# Función para verificar si los ojos están abiertos
def detectar_parpadeo(imagen):
    gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    for rect in rects:
        shape = predictor(gray, rect)
        left_eye = [shape.part(i) for i in range(36, 42)]
        right_eye = [shape.part(i) for i in range(42, 48)]
        
        def ojo_abierto(ojo):
            vertical = abs(ojo[1].y - ojo[5].y)
            return vertical > 2  # umbral simple para detectar apertura

        if ojo_abierto(left_eye) and ojo_abierto(right_eye):
            return True
    return False

# Crear base de datos
ruta = "Empleados"
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f"{ruta}/{nombre}")
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

# Codificar imágenes
def codificar(imagenes):
    lista_codificada = []
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        codificado = fr.face_encodings(imagen)[0]
        lista_codificada.append(codificado)
    return lista_codificada

# Registrar ingresos
def registrar_ingresos(persona):
    with open("registrar_ingresos.csv", "r+") as f:
        lista_datos = f.readlines()
        nombre_registro = [linea.split(",")[0] for linea in lista_datos]

        if persona not in nombre_registro:
            ahora = datetime.now().strftime("%H:%M:%S")
            f.writelines(f"\n{persona},{ahora}")

# Codificar empleados
lista_empleados_codificada = codificar(mis_imagenes)

# Capturar imagen
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)
exito, imagen = captura.read()

if not exito:
    print("No se ha podido tomar la captura")
else:
    cara_captura = fr.face_locations(imagen)
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)
        indice_coincidencia = np.argmin(distancias)

        if distancias[indice_coincidencia] > 0.6 or not detectar_parpadeo(imagen):
            print("No coincide o no se detectó parpadeo.")
        else:
            nombre = nombres_empleados[indice_coincidencia]
            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            registrar_ingresos(nombre)
            cv2.imshow("imagen web", imagen)
            cv2.waitKey(0)
