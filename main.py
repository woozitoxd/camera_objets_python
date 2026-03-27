# main.py
import cv2
from src.camera import Camera
from src.detector import ObjectDetector

def main():
    # 1. Inicializar la cámara y el modelo
    print("Iniciando cámara")
    cam = Camera(camera_index=0)
    detector = ObjectDetector('yolov8n.pt')
    print("Tocar la tecla 'q' en la ventana de video para salir.")

    # 2. Bucle principal de procesamiento
    while True:
        frame = cam.get_frame()
        if frame is None:
            print("Error: No se pudo leer el frame de la cámara.")
            break

        # 3. Detectar objetos en el frame actual
        results = detector.detect(frame)

        # 4. Dibujar los recuadros en el frame
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Obtener coordenadas del recuadro (x1, y1, x2, y2)
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Obtener la clase del objeto y su nivel de confianza
                cls = int(box.cls[0])
                conf = float(box.conf[0])
                class_name = detector.model.names[cls]

                # Dibujar el recuadro en el video
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                #cv2.circle(frame, (x1, y1), 2, (255, 0, 0), 2)


                # Escribir el nombre de la clase y el porcentaje
                label = f"{class_name} {conf:.2f}"
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # 5. Mostrar el video procesado en pantalla
        cv2.imshow('Deteccion de Objetos en Tiempo Real', frame)

        # 6. Escuchar el teclado para salir (tecla 'q')
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 7. Limpiar los recursos al terminar
    cam.release()
    print("Programa finalizado correctamente.")

if __name__ == "__main__":
    main()