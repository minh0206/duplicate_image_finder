import os
import shutil

from dif import dif
from QtImageViewer import QtImageViewer
from ui import Ui_MainWindow
from PyQt5 import QtWidgets, QtGui

from PyQt5.QtCore import QDir, pyqtSlot, Qt
from PyQt5.QtWidgets import (
    QFileDialog,
    QFileDialog,
    QMessageBox,
    QHBoxLayout,
    QListWidgetItem,
    QShortcut,
)
from worker import workerThread


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.centralwidget.setFocus()
        self.ui.btnOpenFolder.clicked.connect(self.openFolder)  # type: ignore

        # Define global variables
        self.movePath = None
        self.currentThread = None

        # init UI
        self.viewer1 = QtImageViewer()
        self.viewer2 = QtImageViewer()
        layout1 = QHBoxLayout()
        layout2 = QHBoxLayout()
        layout1.addWidget(self.viewer1)
        layout2.addWidget(self.viewer2)
        self.ui.viewer1.setLayout(layout1)
        self.ui.viewer2.setLayout(layout2)

        # sinal
        self.ui.srcList.currentItemChanged.connect(self.srcListItemClicked)
        self.ui.dupList.currentItemChanged.connect(self.dupListItemClicked)
        self.shortcut = QShortcut(QtGui.QKeySequence("Ctrl+D"), self)
        self.shortcut.activated.connect(self.deleteImg)

        self.ui.btnMove.clicked.connect(self.moveImg)
        self.ui.btnSelectFolder.clicked.connect(self.selectFolder)
        self.ui.btnDelete.clicked.connect(self.deleteImg)

    def findDuplicate(self, folder):
        # Pass the function to execute
        self.currentThread = workerThread(
            self.findDuplicateThread, folder
        )  # Any other args, kwargs are passed to the run function

        self.currentThread.signals.result.connect(self.finishedSearch)

        # Execute
        self.currentThread.start()

    def finishedSearch(self, result):
        if result:
            _, value = zip(*result.items())
            items = list(map(lambda match: ListWidgetItem(match), value))

            for item in items:
                self.ui.srcList.addItem(item)
        else:
            message = "No duplicate image found in this folder"
            QMessageBox.information(self, "Search result", message)

    def findDuplicateThread(self, folder):
        search = dif(folder)
        return search.result

    @pyqtSlot(QListWidgetItem)
    def srcListItemClicked(self, item):
        if item:
            self.viewer1.open(item.text())

            self.ui.dupList.clear()

            for i in item.matches:
                itm = QListWidgetItem(i["location"])
                itm.mse = i["mse"]

                self.ui.dupList.addItem(itm)

            self.ui.dupList.setCurrentRow(0)

    @pyqtSlot(QListWidgetItem)
    def dupListItemClicked(self, item):
        if item:
            self.viewer2.open(item.text())

    @pyqtSlot(QListWidgetItem)
    def fileSelected(self, item):
        parent = item.parent()
        if parent:
            self.viewer1.open(parent.result["location"])
            print(parent.result["location"])

        self.viewer2.open(item.result["location"])
        print(item.result["location"])

    @pyqtSlot()
    def openFolder(self):
        # Clear existing files
        self.ui.srcList.clear()

        # Open file dialog to get the path
        path = QFileDialog.getExistingDirectory(
            self,
            "Open Folder",
            QDir.currentPath(),
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks,
        )

        if path:
            self.findDuplicate(path)

    def selectFolder(self):
        path = QFileDialog.getExistingDirectory(
            self,
            "Open Folder",
            QDir.currentPath(),
            QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks,
        )

        self.movePath = path
        self.ui.lbFileDestination.setText(path)

    def moveImg(self):
        if self.movePath == None:
            self.selectFolder()
        else:
            dupItem = self.ui.dupList.currentItem()
            self.updateSrcList()

            if dupItem != None:
                try:
                    shutil.move(dupItem.text(), self.movePath)
                except OSError as error:
                    print(error)
                    print("File path can not be moved")

        self._validate()

    def deleteImg(self):
        dupItem = self.ui.dupList.currentItem()

        if dupItem != None:
            message = "Are you sure you want to delete this image"
            ret = QMessageBox.warning(
                self,
                "Delete",
                message,
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )

            # ret = QMessageBox.Yes

            if ret == QMessageBox.Yes:
                self.updateSrcList()

                try:
                    os.remove(dupItem.text())
                except OSError as error:
                    print(error)
                    print("File path can not be removed")

        self._validate()

    def updateSrcList(self):
        # Take and delete
        row = self.ui.dupList.currentRow()
        dupItem = self.ui.dupList.takeItem(row)

        # Take without delete
        srcItem = self.ui.srcList.currentItem()

        matches = srcItem.matches

        for i, match in enumerate(srcItem.matches):
            if match["location"] == dupItem.text():
                matches = self.tupleRemove(matches, i)
                break

        srcItem.matches = matches

    def tupleRemove(self, tupleObj, index):
        return tupleObj[:index] + tupleObj[index + 1 :]

    def _validate(self):
        icon = QtGui.QIcon("check-mark.png")

        item = self.ui.srcList.currentItem()

        if item != None and len(item.matches) == 0:
            self.ui.srcList.currentItem().setBackground(QtGui.QColor(153, 255, 153))
            self.ui.srcList.currentItem().setIcon(icon)

            row = self.ui.srcList.currentRow()
            item = self.ui.srcList.takeItem(row)

            self.ui.srcList.addItem(item)

        dupItem = self.ui.dupList.currentItem()
        if dupItem == None:
            self.viewer2.clearImage()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Left:
            self.ui.srcList.setFocus()
        if event.key() == Qt.Key_Right:
            self.ui.dupList.setFocus()


class ListWidgetItem(QListWidgetItem):
    def __init__(self, result):
        super().__init__()

        _, self.matches = zip(*result["matches"].items())

        self.setText(result["location"])
