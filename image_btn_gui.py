from PySide6 import QtWidgets,QtGui

class PicButton(QtWidgets.QPushButton):
    def __init__(self, parent=None, img_path = None):
        QtWidgets.QPushButton.__init__(self, parent)
        self.set_img(img_path)

    def set_img(self, path):
        pix = QtGui.QPixmap(path)
        img = QtGui.QIcon(pix)
        self.setIcon(img)
        self.setIconSize(pix.size()/10)