import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QPixmap, QFont, QPalette, QColor
from PyQt5.QtCore import Qt, QPoint

class MarcadorPuntaje(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configurar la ventana principal sin marco
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)  # Hacer el fondo transparente
        self.setGeometry(100, 100, 1000, 170)

        # Crear un widget central para el contenido
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Variables para el arrastre de la ventana
        self.dragging = False
        self.offset = QPoint()

        # Crear campos de texto para los nombres de los jugadores
        self.jugador1_input = QLineEdit(self.central_widget)
        self.jugador1_input.setFont(QFont("Arial", 25))
        self.jugador1_input.setGeometry(75, 40, 200, 45)
        self.jugador1_input.setStyleSheet("background-color: red; color: white;")

        self.jugador2_input = QLineEdit(self.central_widget)
        self.jugador2_input.setFont(QFont("Arial", 25))
        self.jugador2_input.setGeometry(725, 40, 200, 45)
        self.jugador2_input.setStyleSheet("background-color: blue; color: white;")

        # Crear contador de puntos para cada jugador
        self.puntos_jugador1 = 0
        self.puntos_jugador2 = 0

        self.puntos_label1 = QLabel("0", self.central_widget)
        self.puntos_label1.setFont(QFont("Arial", 22))
        self.puntos_label1.setGeometry(300, 50, 16, 30)
        self.puntos_label1.setStyleSheet("background-color: red; color: white;")

        self.puntos_label2 = QLabel("0", self.central_widget)
        self.puntos_label2.setFont(QFont("Arial", 22))
        self.puntos_label2.setGeometry(680, 50, 16, 30)
        self.puntos_label2.setStyleSheet("background-color: blue; color: white;")

        self.UPGOP_label = QLabel("UPGOP", self.central_widget)
        self.UPGOP_label.setFont(QFont("Arial Black", 14))
        self.UPGOP_label.setGeometry(470, 150, 76, 20)
        self.UPGOP_label.mousePressEvent = self.close_application
        self.UPGOP_label.setStyleSheet("background-color: white; color: black;")

        # Cargar y mostrar el logo del evento
        self.logo = QLabel(self.central_widget)
        pixmap = QPixmap("logo.png")  # Ajusta la ruta de la imagen si es necesario
        pixmap = pixmap.scaled(150, 150, Qt.KeepAspectRatio)  # Ajustar tamaño sin distorsión
        self.logo.setPixmap(pixmap)
        self.logo.setGeometry(430, 0, 150, 150)  # Coordenadas originales
        self.logo.setAlignment(Qt.AlignCenter)  # Centra la imagen
        self.logo.mousePressEvent = self.resetear_puntaje  # Conectar clic al logo a la función de restablecimiento

        # Botones para incrementar los puntos
        self.incrementar_puntos1_button = QPushButton("+", self.central_widget)
        self.incrementar_puntos1_button.setFont(QFont("Arial", 22))
        self.incrementar_puntos1_button.setGeometry(320, 50, 20, 30)
        self.incrementar_puntos1_button.clicked.connect(self.incrementar_puntos_jugador1)

        self.incrementar_puntos2_button = QPushButton("+", self.central_widget)
        self.incrementar_puntos2_button.setFont(QFont("Arial", 22))
        self.incrementar_puntos2_button.setGeometry(655, 50, 20, 30)
        self.incrementar_puntos2_button.clicked.connect(self.incrementar_puntos_jugador2)

    def incrementar_puntos_jugador1(self):
        self.puntos_jugador1 += 1
        self.puntos_label1.setText(str(self.puntos_jugador1))

    def incrementar_puntos_jugador2(self):
        self.puntos_jugador2 += 1
        self.puntos_label2.setText(str(self.puntos_jugador2))

    def resetear_puntaje(self, event):
        self.puntos_jugador1 = 0
        self.puntos_jugador2 = 0
        self.puntos_label1.setText(str(self.puntos_jugador1))
        self.puntos_label2.setText(str(self.puntos_jugador2))

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(self.mapToGlobal(event.pos() - self.offset))

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False
    
    def close_application(self, event):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MarcadorPuntaje()
    window.show()
    sys.exit(app.exec_())
