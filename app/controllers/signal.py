# PyQt imports
from PyQt5.QtWidgets import QWidget

# Components imports
# noinspection PyUnresolvedReferences
from components.signal.signal_ui import Ui_signalW


class SignalGraph(QWidget, Ui_signalW):
    """
    Signals viewer
    """

    def __init__(self):
        # Generar los widgets
        super().__init__()
        self.setupUi(self)
