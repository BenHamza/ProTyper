from PySide.QtCore import QThread
from auto_press import ProTyper
import time

class TypeItWorker(QThread):

    def __init__(self, text, tray):
        QThread.__init__(self)
        self.text = text
        self.tray = tray

    def __del__(self):
        self.wait()

    def run(self):
        for x in range(3, 0, -1):
            self.tray.showMessage('Get Ready', 'Autotype will start in ' + str(x) + ' seconds.',
                                  self.tray.Information, 100)
            time.sleep(1)

        p = ProTyper(self.text, 0, 3, 0)
        p.start_auto_type()