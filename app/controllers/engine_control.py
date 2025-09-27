# PyQt imports
from PyQt5.QtWidgets import QWidget

# Components imports
# noinspection PyUnresolvedReferences
from components.engineControl.engineControl_ui import Ui_engineControlW


class EngineControl(QWidget, Ui_engineControlW):
    """
    Engine control viewer
    """

    def __init__(self):
        # Generar los widgets
        super().__init__()
        self.setupUi(self)
