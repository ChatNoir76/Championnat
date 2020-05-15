# -*- coding: utf-8 -*-
# start_app.py
# utilisation de Qt designer

import sys

from PyQt5.QtWidgets import QApplication
from fenetre import MainWindow


app = QApplication(sys.argv)

fen = MainWindow()
fen.show()

rc = app.exec_()
sys.exit(rc)

