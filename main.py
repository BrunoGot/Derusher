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
from image_btn_gui import PicButton


"""class MainView(QtWidgets.QWidget):
    def __init__(self):
        pass"""
class ImageDerushGui(QtWidgets.QWidget):
    READ_FORMATS = ["jpg","png"]
    SAVE_FOLDER_NAME = "selection"

    def __init__(self, path):
        super().__init__()
        self.current_index = 0
        #path=r"I:\01_Rush\Rush\Raven\ShootRaven\19_12_2022\selectionA"
        self.path = path
        self.save_folder = self.create_folder(self.SAVE_FOLDER_NAME)
        self.imgs = self.load_folder(self.path) #[r"I:\01_Rush\Rush\Raven\ShootRaven\19_12_2022\DSC05180.JPG"]
        ##layout
        self.main_layout = QtWidgets.QVBoxLayout()
        #img#
        self.pic_btn = PicButton(img_path = self.get_current_img())
        self.main_layout.addWidget(self.pic_btn)
        ##
        #actions btn#
        self.open_folder_btn = QtWidgets.QPushButton("Open Folder")
        self.open_folder_btn.clicked.connect(self.open_folder)
        self.main_layout.addWidget(self.open_folder_btn)

        self.img_name_txt = QtWidgets.QLineEdit("name")
        self.main_layout.addWidget(self.img_name_txt)
        self.nav_layout = QtWidgets.QHBoxLayout()
        self.prev_btn = QtWidgets.QPushButton("<<")
        self.prev_btn.clicked.connect(self.prev_img)
        self.nav_layout.addWidget(self.prev_btn)
        self.next_btn = QtWidgets.QPushButton(">>")
        self.next_btn.clicked.connect(self.next_img)
        self.nav_layout.addWidget(self.next_btn)
        self.main_layout.addLayout(self.nav_layout)
        self.select_btn = QtWidgets.QPushButton("Select")
        self.select_btn.clicked.connect(self.save_img)
        self.main_layout.addWidget(self.select_btn)
        ##
        self.setLayout(self.main_layout)
        ##

    def next_img(self):
        self.current_index =(self.current_index+1)%(len(self.imgs)-1)

        self.pic_btn.set_img(self.get_current_img())
        self.img_name_txt.setText(self.imgs[self.current_index])

    def prev_img(self):
        #todo:fusion avec next image
        self.current_index -=1
        self.pic_btn.set_img(self.get_current_img())
        self.img_name_txt.setText(self.imgs[self.current_index])

    def load_folder(self,path):
        print("load folder : {}".format(path))
        if not path:
            return
        imgs = []
        files = os.listdir(path)

        print("load folder : files : {}".format(files))
        for i in files:
            ext = os.path.splitext(i)[1].replace(".","")
            print("load folder : ext : {}".format(ext))
            if ext.lower() in self.READ_FORMATS:
                print("append image")
                imgs.append(i)
        return imgs

    def get_current_img(self):
        return os.path.join(self.path,self.imgs[self.current_index])

    def save_img(self):
        if not self.save_folder:
            self.save_folder = self.create_folder(self.SAVE_FOLDER_NAME)

        img_path = self.get_current_img()
        saved_img_path = os.path.join(self.save_folder,self.imgs[self.current_index])
        shutil.copy(img_path,saved_img_path)
        print("image saved")

    def create_folder(self,folder_name):
        """
        create a local folder
        """
        try:
            path = os.path.join(self.path,folder_name)
            if not os.path.isdir(path):
                os.mkdir(path)
            print("path = {}".format(path))
            return path

        except Exception as e:
            print("NO PATH !! : {}".format(e))

    def open_folder(self):
        os.system(f'start {self.path}')

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
