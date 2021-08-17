from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.core.window import Window

from CalcCore import CalcCore

Window.size = (300, 372)


class Container(BoxLayout):
    calc_text = StringProperty(defaultvalue='0')

    def __init__(self):
        self._core = CalcCore()
        super(Container, self).__init__()
        for x in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'C', 'plus', 'minus', 'multi', 'div', 'eq'):
            self.ids['button_{}'.format(x)].bind(state=self._callback)

    def _callback(self, instance, value):
        if value == 'down':
            if instance.text == '=':
                self._core.calc()
            elif instance.text == 'C':
                self._core.clear()
            else:
                self._core.addChar(instance.text)
            self._display()

    def _display(self):
        self.calc_text = self._core.text


class CalcApp(App):
    def build(self):
        self.icon = 'calculator.png'
        return Container()


if __name__ == '__main__':
    CalcApp().run()
