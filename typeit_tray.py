from lib2to3.pgen2.tokenize import generate_tokens

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
        self.menu.addAction(self.open_act)
        self.menu.addAction(self.stop_act)
        self.menu.addSeparator()
        self.menu.addAction(self.close_act)
        self.tray.setContextMenu(self.menu)
        self.tray.show()

    def open(self):
        pass
        #get_ui_manager().showNormal()

    def stop_auto_type(self):
        pass
        #get_ui_manager().typeit_thread.stop()

    def close(self):
        from typeit_main import get_ui_manager
        get_ui_manager().close()

    def createActions(self):
        self.open_act = QAction('Open TypeIt', self,
                                statusTip="Cut the current selection's contents to the clipboard",
                                triggered=self.open)

        self.close_act = QAction("Close TypeIt", self,
                                 statusTip="Copy the current selection's contents to the clipboard",
                                 triggered=self.close)

        self.stop_act = QAction('Stop Typing..', self,
                                shortcut= QKeySequence('Ctrl+Q'),
                                statusTip="Cut the current selection's contents to the clipboard",
                                triggered=self.stop_auto_type)


    def focusInEvent(self, event):
        self.activateWindow()

    def focusOutEvent(self, event):
        self.hide()


class TrayIcon(QSystemTrayIcon):
    def __init__(self):
        super(TrayIcon, self).__init__()
        self.menu = TrayMenu()
        self.setIcon(QIcon('key.png'))
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
