from PyQt5.QtWidgets import QDialog
from view.ui.Ui_addplayer import Ui_Dialog_addplayer


class AddPlayerWindow(QDialog, Ui_Dialog_addplayer):
    def __init__(self, parent=None):
        super(AddPlayerWindow, self).__init__(parent)
        self.setupUi(self)

    def get_fname(self):
        return self.textEdit_fname.toPlainText()

    def get_lname(self):
        return self.textEdit_lname.toPlainText()
