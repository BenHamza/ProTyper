from PySide import QtGui, QtCore


class TrayMenu(QtGui.QWidget):
    def __init__(self):
        super(TrayMenu, self).__init__()
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        self.setGeometry(100, 100, 650, 650)

        self.button = QtGui.QPushButton('Test')
        self.button1 = QtGui.QPushButton('Test')
        self.button2 = QtGui.QPushButton('Test')

    def focusInEvent(self, event):
        self.activateWindow()

    def focusOutEvent(self, event):
        self.hide()


class TrayIcon(QtGui.QSystemTrayIcon):
    def __init__(self):
        super(TrayIcon, self).__init__()
        self.menu = TrayMenu()
        self.activated.connect(self.activate_tray_menu)
        self.setIcon(QtGui.QIcon('key.png'))
        self.show()

    def activate_tray_menu(self, reason):
        if reason is QtGui.QSystemTrayIcon.Context:
            self.custom_menu()

    def custom_menu(self):
        pos = self.geometry().topRight()
        x, y = pos.x() - self.menu.width() / 2, pos.y() - self.menu.height()
        self.menu.move(x, y)
        self.menu.show()
        self.menu.setFocus()
