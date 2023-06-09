# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 719)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.grid = QtWidgets.QGridLayout()
        self.grid.setObjectName("grid")
        self.srcList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.srcList.sizePolicy().hasHeightForWidth())
        self.srcList.setSizePolicy(sizePolicy)
        self.srcList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.srcList.setObjectName("srcList")
        self.grid.addWidget(self.srcList, 6, 0, 1, 1)
        self.viewer2 = QtWidgets.QWidget(self.centralwidget)
        self.viewer2.setObjectName("viewer2")
        self.grid.addWidget(self.viewer2, 7, 1, 1, 1)
        self.srcLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.srcLabel.setFont(font)
        self.srcLabel.setObjectName("srcLabel")
        self.grid.addWidget(self.srcLabel, 3, 0, 1, 1)
        self.viewer1 = QtWidgets.QWidget(self.centralwidget)
        self.viewer1.setObjectName("viewer1")
        self.grid.addWidget(self.viewer1, 7, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.grid.addLayout(self.horizontalLayout_3, 5, 1, 1, 1)
        self.dupList = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dupList.sizePolicy().hasHeightForWidth())
        self.dupList.setSizePolicy(sizePolicy)
        self.dupList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dupList.setObjectName("dupList")
        self.grid.addWidget(self.dupList, 6, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnOpenFolder = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenFolder.setEnabled(True)
        self.btnOpenFolder.setObjectName("btnOpenFolder")
        self.horizontalLayout_2.addWidget(self.btnOpenFolder)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.grid.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnMove = QtWidgets.QPushButton(self.centralwidget)
        self.btnMove.setObjectName("btnMove")
        self.horizontalLayout.addWidget(self.btnMove)
        self.btnDelete = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelete.setObjectName("btnDelete")
        self.horizontalLayout.addWidget(self.btnDelete)
        self.btnSelectFolder = QtWidgets.QPushButton(self.centralwidget)
        self.btnSelectFolder.setObjectName("btnSelectFolder")
        self.horizontalLayout.addWidget(self.btnSelectFolder)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lbFileDestination = QtWidgets.QLabel(self.centralwidget)
        self.lbFileDestination.setObjectName("lbFileDestination")
        self.horizontalLayout.addWidget(self.lbFileDestination)
        self.grid.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.dupLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dupLabel.setFont(font)
        self.dupLabel.setObjectName("dupLabel")
        self.horizontalLayout_5.addWidget(self.dupLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.grid.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.grid)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.srcLabel.setText(_translate("MainWindow", "Sources"))
        self.btnOpenFolder.setText(_translate("MainWindow", "Open folder"))
        self.btnMove.setText(_translate("MainWindow", "Move"))
        self.btnDelete.setText(_translate("MainWindow", "Delete"))
        self.btnSelectFolder.setText(_translate("MainWindow", "Select folder"))
        self.lbFileDestination.setText(_translate("MainWindow", "No destination"))
        self.dupLabel.setText(_translate("MainWindow", "Duplicates"))
        self.label.setText(_translate("MainWindow", "Move to"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
