# camera_objets_python

Proyecto que detecta objetos en tiempo real usando la cámara web y un modelo de inteligencia artificial (YOLOv8).

## Qué hace

El programa abre la webcam y analiza cada frame del video en tiempo real con el modelo YOLOv8. Cuando detecta un objeto (personas, celulares, botellas, etc.) lo marca con un recuadro y muestra el nombre del objeto junto con el porcentaje de confianza. Para cerrar el programa se toca la tecla **q** en la ventana del video.

## Dependencias

| Paquete | Versión | Descripción |
|---|---|---|
| **ultralytics** | 8.4.30 | Framework de YOLO, se usa para cargar y correr el modelo de detección de objetos. |
| **opencv-python** | 4.13.0.92 | Maneja la cámara, captura los frames, dibuja los recuadros y muestra la ventana de video. |
| **numpy** | 2.4.3 | Librería base para manejo de arrays y matrices, la usan OpenCV y Ultralytics por detrás. |
