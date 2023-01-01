import os

from PySide6 import QtWidgets
import shutil

from image_btn_gui import PicButton

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
