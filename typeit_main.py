import sys
import time

from PySide.QtCore import *
from PySide.QtGui import *
from worker import TypeItWorker

from GUI import protyper
from typeit_tray import TrayIcon
import Queue as queue


class MainApp(QMainWindow, protyper.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)
        self.setupUi(self)
        self.installEventFilter(self)

        self.tray = TrayIcon()
        self.typeit_thread = None

        self.makeClickable(self.pix_key_text_3)

        QObject.connect(self.pix_key_text_3, SIGNAL("clicked()"), self.slide_up)

        self.scale_up(self.pix_key_text_3)


        # self.an = QPropertyAnimation(self.pix_key, "pos")
        # self.an.setDuration(1500)
        # self.an.setStartValue(self.pix_key)
        # self.an.setEndValue(self.plainTextEdit.pos())

        # self.an.start()
        # Declare graphics effect for splash fade_out
        # self.effect = QGraphicsOpacityEffect()
        # self.pix_key.setGraphicsEffect(self.effect)
        # QGraphicsOpacityEffect.setOpacity(self.effect, 1)

        # self.anim_group = QSequentialAnimationGroup()
        # self.anim_group.addPause(200)
        # self.anim_group.addAnimation(self.fade_out(self.effect, 200))
        # self.anim_group.start()
        # self.ag.finished.connect(self.pixmap_splash.deleteLater)

    def handle_result(self, result):
        val = result.val
        if val == 'show':
            self.showNormal()
        print("got val {}".format(val))
        # You can update the UI from here.

    def start(self):
        self.queue = queue.Queue()
        self.showMinimized()
        self.typeit_thread = TypeItWorker(self.read_plain(), self.tray, self.queue, self.handle_result)
        self.typeit_thread.start()



    def read_plain(self):
        return self.plain_text.toPlainText()

    def show_window(self):
        self.showNormal()

    @staticmethod
    def fade_in(target, duration):
        an = QPropertyAnimation(target, "opacity")
        an.setDuration(duration)
        an.setStartValue(0)
        an.setEndValue(1)
        return an

    @staticmethod
    def fade_out(target, duration):
        an = QPropertyAnimation(target, "opacity")
        an.setDuration(duration)
        an.setStartValue(1)
        an.setEndValue(0)
        return an

    def scale_up(self, target=None):
        target = self.pix_key_text_3
        a = QPropertyAnimation(target, "size", self)
        a.setDuration(100)
        a.setStartValue(target.width())
        a.setEndValue(0)
        a.start(QPropertyAnimation.DeleteWhenStopped)

    def scale_down(self):
        target = self.pix_key_text_3
        an = QPropertyAnimation(target, "size")
        # self.e.setStartValue()
        an.setEndValue(QSize(target.width() - 25, target.height() - 25))
        an.start()
        an.finished.connect(self.scale_up())

        return an

    def slide_up(self):
        self.an = QPropertyAnimation(self.pix_key_text_3, "pos")
        # self.e.setStartValue()
        self.an.setEndValue(QPointF(self.pix_key_text_3.x(), 0))
        self.an.start()
        self.ab = QPropertyAnimation(self.plain_text, "pos")
        # self.e.setStartValue()
        self.ab.setEndValue(QPointF(self.plain_text.x(), 150))
        self.ab.start()
        self.ac = QPropertyAnimation(self.label_start, "pos")
        # self.e.setStartValue()
        self.ac.setEndValue(QPointF(self.label_start.x(), 200))
        self.ac.start()

        self.plain_text.setFocus()
        # self.pix_key_text_3.setPixmap(QPixmap(":/images/key_enter.png"))

    def slide_left(self):
        self.an = QPropertyAnimation(self.pix_key_text_3, "pos")
        # self.e.setStartValue()
        self.an.setEndValue(QPointF(self.pix_key_text_3.x() - 200, self.pix_key_text_3.y()))
        self.an.start()

    def makeClickable(self, widget):
        def SendClickSignal(widget, evnt):
            widget.emit(SIGNAL('clicked()'))

        widget.mousePressEvent = lambda evnt: SendClickSignal(widget, evnt)

    def eventFilter(self, widget, event):
        if event.type() == QEvent.KeyPress:
            # and widget is self.edit:
            key = event.key()
            if key == Qt.Key_Escape:
                self.close()
            if key == Qt.Key_Up:
                self.slide_up()
            if key == Qt.Key_Left:
                self.slide_left()
            if key == Qt.Key_F12:
                self.start()
            if key == QKeySequence.Quit:
                self.typeit_thread.stop()
                # else:
                # if key == Qt.Key_Return:
                # self.edit.setText('return')
                # elif key == Qt.Key_Enter:
                # self.edit.setText('enter')
                return True
        return QWidget.eventFilter(self, widget, event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, QEvent(QEvent.NonClientAreaMouseButtonPress))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeEvent(self, event):
        self.tray = None
        self.close()


#__MY_SINGLETON = MainApp()

#def get_ui_manager():
    #return __MY_SINGLETON


def main():
    app = QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()