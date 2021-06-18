#!/urs/bin/python3
#-*- coding : utf-8 -*-

import sys
from CalcCore import CalcCore

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

class CalcApp(QWidget):

    def __init__(self):
        self._initUI()
        self._initEvents()
        self._core = CalcCore(self._ui.l_display.text())
        self._ui.show()

    def _initUI(self):
        self._ui = uic.loadUi("calc.ui")

    def _initEvents(self):
        self._initClickEvent(self._ui.btn_0)
        self._initClickEvent(self._ui.btn_1)
        self._initClickEvent(self._ui.btn_2)
        self._initClickEvent(self._ui.btn_3)
        self._initClickEvent(self._ui.btn_4)
        self._initClickEvent(self._ui.btn_5)
        self._initClickEvent(self._ui.btn_6)
        self._initClickEvent(self._ui.btn_7)
        self._initClickEvent(self._ui.btn_8)
        self._initClickEvent(self._ui.btn_9)

        self._initClickEvent(self._ui.btn_plus)
        self._initClickEvent(self._ui.btn_minus)
        self._initClickEvent(self._ui.btn_mult)
        self._initClickEvent(self._ui.btn_div)
        self._initClickEvent(self._ui.btn_eq)
        self._initClickEvent(self._ui.btn_clear)

    def _initClickEvent(self, btn):
        if btn == self._ui.btn_eq:
            btn.clicked.connect(lambda: self._calc())
        elif btn == self._ui.btn_clear:
            btn.clicked.connect(lambda: self._clear())
        else:
            btn.clicked.connect(lambda: self._clickChar(btn.text()))

    def _clickChar(self, char):
        self._core.addChar(char)
        self._display()

    def _calc(self):
        self._core.calc()
        self._display()

    def clear(self):
        self._core.clear()
        self._display()

    def _display(self):
        self._ui.l_display.setText(self._core.text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CalcApp()
    app.exec_()