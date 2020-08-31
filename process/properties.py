from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


from node_editor.utils import dumpException
# import click


DEBUG = False
DEBUG_CONTEXT = False

class PropertiesPanel(QDockWidget):
    def __init__(self):
        super().__init__()
        self.click=click.clickWindow



        self.propertytab()


    def propertytab(self,controls="none"):
        self.nodesListWidget2 = QListWidget()
        self.nodesDock2 = QDockWidget("")
        if controls == "none":

            self.nodesDock2.setWidget(self.nodesListWidget2)
        else:
            self.nodesDock2 = QDockWidget("Properties")
            self.nodesDock2.setWidget(self.click)

        self.nodesDock2.widget().setMinimumSize(QSize(350, 800))
        # self.nodesDock2.setWidget(self.nodesListWidget2)
        self.nodesDock2.setFloating(False)

        self.addDockWidget(Qt.RightDockWidgetArea, self.nodesDock2)

