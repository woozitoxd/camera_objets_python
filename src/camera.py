# src/camera.py
import cv2

class Camera:
    def __init__(self, camera_index=0):
        """Inicializa la cámara web."""
        self.cap = cv2.VideoCapture(camera_index)
        if not self.cap.isOpened():
            raise ValueError("No se pudo acceder a la cámara.")

    def get_frame(self):
        """Lee y devuelve un frame de la cámara."""
        ret, frame = self.cap.read()
        if not ret:
            return None
        return frame

    def release(self):
        """Libera la cámara y destruye las ventanas de OpenCV."""
        self.cap.release()
        cv2.destroyAllWindows()