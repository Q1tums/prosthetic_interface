# PyQt imports
from PyQt5.QtWidgets import QWidget

# Components imports
# noinspection PyUnresolvedReferences
from components.serialConn.serialConn_ui import Ui_serialConnW


class SerialConn(QWidget, Ui_serialConnW):
    """
    Serial ports viewer
    """

    def __init__(self):
        # Generar los widgets
        super().__init__()
        self.setupUi(self)
