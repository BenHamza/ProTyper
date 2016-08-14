from PySide.QtCore import *
from auto_press import ProTyper
import time
from result_obj import ResultObj



class TypeItWorker(QThread):
    finished =  Signal(object)

    def __init__(self, text, tray, queue, callback):
        QThread.__init__(self)
        self.text = text
        self.tray = tray
        self.queue = queue
        self.finished.connect(callback)

    def __del__(self):
        self.wait()

    def run(self):
        for x in range(3, 0, -1):
            self.tray.showMessage('Get Ready!', 'Autotype will start in ' + str(x) + ' seconds.',
                                  self.tray.Information, 100)
            time.sleep(1)
        self.tray.showMessage('Started!', 'TypeIt bot is pressing the keys.',
                              self.tray.Information, 1)

        p = ProTyper(self.text, 0, 0, 0)

        if p.start_auto_type():
            self.tray.showMessage('Task Completed :D', 'All keys has been pressed.',
                                  self.tray.Information, 1)

        self.finished.emit(ResultObj('show'))



