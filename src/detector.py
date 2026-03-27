# src/detector.py
from ultralytics import YOLO

class ObjectDetector:
    def __init__(self, model_version='yolov8n.pt'):
        """
        Carga el modelo YOLO. 
        Si 'yolov8n.pt' no está en la PC, se descargará automáticamente la primera vez.
        """
        self.model = YOLO(model_version)

    def detect(self, frame):
        """
        Recibe un frame de video y devuelve los resultados de la detección.
        Se usa stream=True para optimizar el rendimiento en video.
        """
        results = self.model(frame, stream=True, verbose=False)
        return results