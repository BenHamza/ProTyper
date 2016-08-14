from PySide.QtCore import *

class ResultObj(QObject):
    def __init__(self, val):
        self.val = val