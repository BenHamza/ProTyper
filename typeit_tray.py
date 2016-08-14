from PySide.QtCore import *
from PySide.QtGui import *


class TrayMenu(QWidget):
    def __init__(self):
        super(TrayMenu, self).__init__()
        self.setFocusPolicy(Qt.StrongFocus)
        self.menu = None

        self.tray = QSystemTrayIcon(QIcon('key.png'), self)
        self.createActions()
        self.populate_context()

    def populate_context(self):
        self.menu = QMenu()
        self.menu = QMenu(self)
        self.menu.addAction(self.open_act)
        self.menu.addSeparator()
        self.menu.addAction(self.close_act)
        self.tray.setContextMenu(self.menu)
        self.tray.show()

    def close(self):
        self.close()

    def open(self):
        self.close()

    def createActions(self):
        self.open_act = QAction('Open TypeIt', self,
                                shortcut=QKeySequence.Cut,
                                statusTip="Cut the current selection's contents to the clipboard",
                                triggered=self.open)

        self.close_act = QAction("Close TypeIt", self,
                                 shortcut=QKeySequence.Copy,
                                 statusTip="Copy the current selection's contents to the clipboard",
                                 triggered=self.close)

    def focusInEvent(self, event):
        self.activateWindow()

    def focusOutEvent(self, event):
        self.hide()

    def print1(self):
        'LALALALA'


class TrayIcon(QSystemTrayIcon):
    def __init__(self):
        super(TrayIcon, self).__init__()
        self.menu = TrayMenu()
        self.activated.connect(self.activate_tray_menu)
        self.show()

    def activate_tray_menu(self, reason):
        if reason is QSystemTrayIcon.Context:
            self.custom_menu()

    def custom_menu(self):
        pos = self.geometry().topRight()
        x, y = pos.x() - self.menu.width() / 2, pos.y() - self.menu.height()
        self.menu.move(x, y)
        self.menu.show()
        self.menu.setFocus()
