# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.

#Derusher : Select a folder and sort rush, manually or automatically
#have a selector module where you can view pictures and add the to the work selection, bin or the dump folder

"""
todo:
 - select a folder
 - display image
 - do an action
"""
import os
import sys
import shutil

from PySide6 import QtWidgets, QtGui,QtCore
from PySide6.QtGui import QAction
#import View
#import ConfigView
import file_system as fs
from image_derush_gui import ImageDerushGui


"""class MainView(QtWidgets.QWidget):
    def __init__(self):
        pass"""

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.file_system = fs.FileSystem()
        self.initUI()

    def initUI(self):
        # Menu bar
        menubar = self.menuBar()
        ## Define actions
        exitAction = QAction(QtGui.QIcon("exit.png"), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(self.close)
        #
        option_action = QAction(QtGui.QIcon("exit.png"), '&Options', self)
        option_action.setShortcut('Ctrl+O')
        option_action.setStatusTip("Options")
        option_action.triggered.connect(self.open_config_menu)
        ##add it to the menu
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(option_action)

        #status bar
        self.statusBar()

        #self.default_lib = View.LibraryView()
        """
        self.tab_widget = QtWidgets.QTabWidget()
        self.tab_widget.currentChanged.connect(self.on_tab_changed)
        #self.tab_widget.addTab(self.default_lib,self.file_system.default_config_name)"""
        #Manual Derusher Window
        self.manual_derush_gui = None

        ##Main window##
        self.main_layout = QtWidgets.QVBoxLayout()
        # select a path#
        self.path_selector_btn = QtWidgets.QPushButton("Select path")
        self.path_selector_btn.clicked.connect(self.choose_folder)
        self.path_selector_line = QtWidgets.QLineEdit()
        self.pathSelector_layout = QtWidgets.QHBoxLayout()
        self.pathSelector_layout.addWidget(self.path_selector_line)
        self.pathSelector_layout.addWidget(self.path_selector_btn)
        ##
        # action buttons#
        self.manual_derush_btn = QtWidgets.QPushButton("Manual Derush")
        self.manual_derush_btn.clicked.connect(self.open_manual_dersuh)
        ##
        self.main_layout.addLayout(self.pathSelector_layout)
        self.main_layout.addWidget(self.manual_derush_btn)
        # self.setLayout(self.main_layout)
        #
        self.main_view = QtWidgets.QWidget()
        self.main_view.setLayout(self.main_layout)

        #self.QStackedWidget(self.main_view)
        self.setCentralWidget(self.main_view)
        #self.setGeometry(300,300,250,150)
        self.setWindowTitle('Derusher')
        self.show()

    def open_config_menu(self):
        pass
        #self.config_window = ConfigView.MainView(self)
        #self.config_window.show()

    def add_new_config(self, config_name):
        print("load config : "+config_name)
        #self.tab_widget.addTab(View.LibraryView(config_name), config_name)

    def open_manual_dersuh(self):
        if not self.file_system.folder_path:
            self.file_system.folder_path = self.path_selector_line.text()
        if self.file_system:
            self.manual_derush_gui = ImageDerushGui(self.file_system.folder_path)
            self.manual_derush_gui.show()

    def choose_folder(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(None,"Select Folder")
        self.file_system.folder_path = folder
        self.path_selector_line.setText(folder)

def GUI_Style(app):
    file_qss = open("Styles/Combinear.qss")
    with file_qss:
        qss = file_qss.read()
        #print("QSS = "+qss)
        app.setStyleSheet(qss)

def main():
    app = QtWidgets.QApplication(sys.argv)
    GUI_Style(app)
    ex = MainWindow()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
