
# PyQt imports
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

# Controller import
from controllers.app import MainApp

# Imports
import sys


# Función para verificar si el monitor es 4K
def is_4K():
    # Necesitamos crear una aplicación temporal para obtener la resolución
    temp_app = QApplication(sys.argv)
    screen = temp_app.primaryScreen()
    size = screen.size()
    width = size.width()
    height = size.height()
    print(f"Resolución de la pantalla: {width}x{height}")

    # Eliminamos la aplicación temporal
    temp_app.quit()

    # Retorna True si la resolución es 4K o mayor
    return width >= 3840 and height >= 2160


if __name__ == "__main__":
    # Verifica si el monitor es 4K antes de crear QApplication y activar el High DPI
    if is_4K():
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # enable high dpi scaling
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)  # use high dpi icons
        print("High DPI activado para monitor 4K.")
    else:
        print("High DPI no activado, monitor no es 4K.")

    # Crear la aplicación real después de configurar los DPI
    app = QApplication([])

    # Importamos desde la carpeta ./styles el archivo main.css para establecer estilos
    # app.setStyleSheet(open("./styles/main.css").read())

    main_window = MainApp()
    main_window.show()

    sys.exit(app.exec_())
