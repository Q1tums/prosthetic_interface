# PyQt imports
from PyQt5.QtWidgets import QMainWindow

# Components imports
from components.mainWindow.mainWindow_ui import Ui_MainWindow

# Controllers
from .signal import SignalGraph
from .engine_control import EngineControl
from .serial_conn import SerialConn


class MainApp(QMainWindow, Ui_MainWindow):
    """
    Clase principal de la interfaz de usuario
    """

    def __init__(self):
        # Generar los widgets
        super().__init__()
        self.setupUi(self)

        # Componentes
        self.signal_graph = SignalGraph()
        self.mainContainerLayout.addWidget(self.signal_graph)

        self.serial_conn = SerialConn()
        self.sideContainerLayout.addWidget(self.serial_conn)

        self.engine_control = EngineControl()
        self.sideContainerLayout.addWidget(self.engine_control)
