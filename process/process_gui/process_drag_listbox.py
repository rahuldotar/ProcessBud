from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from process.process_gui.process_conf import *
from node_editor.utils import dumpException


class QDMDragListbox(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # init
        self.setIconSize(QSize(32, 32))
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setDragEnabled(True)

        self.addMyItems()


    def addMyItems(self):
        keys = list(CALC_NODES.keys())
        print(keys)
        keys.sort()
        for key in keys:
            node = get_class_from_opcode(key)
            self.addMyItem(node.op_title, node.icon, node.op_code)


    def addMyItem(self, name, icon=None, op_code=0):
        item = QListWidgetItem(name, self) # can be (icon, text, parent, <int>type)
        pixmap = QPixmap(icon if icon is not None else ".")
        item.setIcon(QIcon(pixmap))
        item.setSizeHint(QSize(32, 32))

        item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsDragEnabled)

        # setup data
        item.setData(Qt.UserRole, pixmap)
        item.setData(Qt.UserRole + 1, op_code)


    def startDrag(self, *args, **kwargs):
        try:
            item = self.currentItem()
            print(item)
            op_code = item.data(Qt.UserRole + 1)
            print(op_code)

            pixmap = QPixmap(item.data(Qt.UserRole))
            print(pixmap)


            itemData = QByteArray()
            dataStream = QDataStream(itemData, QIODevice.WriteOnly)
            print(dataStream)
            dataStream << pixmap
            dataStream.writeInt(op_code)
            dataStream.writeQString(item.text())

            mimeData = QMimeData()
            mimeData.setData(LISTBOX_MIMETYPE, itemData)
            print(mimeData)

            drag = QDrag(self)
            drag.setMimeData(mimeData)
            # drag.setHotSpot(QPoint(pixmap.width() / 2, pixmap.height() / 2))
            # drag.setPixmap(pixmap)

            drag.exec_(Qt.MoveAction)

        except Exception as e: dumpException(e)