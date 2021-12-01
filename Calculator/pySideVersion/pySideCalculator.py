import sys

from Calculator.CalcCore import CalcCore

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader


class PySideApp(QMainWindow):
    """Класс реализации GUI калькулятора с помощью PySide."""

    def __init__(self):
        super(PySideApp, self).__init__()
        self._init_ui()
        self._init_events()
        self._core = CalcCore(self._ui.l_display.text())
        self._ui.show()

    def _init_ui(self):
        self._ui = QUiLoader().load("../ui/calc.ui")
        self._ui.setWindowIcon(QIcon('../../images/AppIcon.png'))

    def _init_events(self):
        for widget in vars(self._ui).values():
            if isinstance(widget, QPushButton):
                self._init_click_event(widget)

    def _init_click_event(self, btn):
        if btn == self._ui.btn_eq:
            btn.clicked.connect(lambda: self._calc())
        elif btn == self._ui.btn_clear:
            btn.clicked.connect(lambda: self._clear())
        else:
            btn.clicked.connect(lambda: self._click_char(btn.text()))

    def _click_char(self, char):
        self._core.add_char(char)
        self._display()

    def _calc(self):
        self._core.calc()
        self._display()

    def _clear(self):
        self._core.clear()
        self._display()

    def _display(self):
        self._ui.l_display.setText(self._core.text)


class CalcApp:
    """Класс запуска GUI калькулятора, реализованного с помощью PySide."""
    def run(self):
        """Запустить калькулятор."""
        app = QApplication(sys.argv)
        ex = PySideApp()
        app.exec()
