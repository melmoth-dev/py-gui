from typing import Final


class CalcCore:
    """Класс ядра логики работы калькулятора."""

    OPERATION_CHARS: Final = ('+', '-', '*', '/')
    """Список допустимых символов операций."""

    def __init__(self, term='0'):
        self._isResult = False
        self._result = '0'
        self.__term = term

    def __get_term(self):
        return self.__term

    def __set_term(self, value):
        self.__term = value
        if self._isResult:
            self._isResult = False

    term = property(fget=__get_term,
                    fset=__set_term,
                    doc="""Свойство, содержащее вычисляемую строку.""")

    @property
    def text(self):
        """Свойство, содержащее отображаемый текст."""
        if self._isResult:
            return self._result
        return self.term

    def _get_calculated_term(self):
        if self.term[-1] in self.OPERATION_CHARS:
            return self.term[:-1]
        else:
            return self.term

    def add_char(self, char):
        """Добавить символ к вычисляемой строке."""
        if self._isResult:
            self.term = self._result
            self.add_char(char)
        elif char in self.OPERATION_CHARS:
            self.term = "%s%s" % (self._get_calculated_term(), char)
        else:
            if self.term == '0':
                self.term = char
            else:
                self.term = "%s%s" % (self.term, char)

    def calc(self):
        """Выполнение расчёт вычисляемой строки."""
        if not self._isResult:
            self._result = str(round(eval(self._get_calculated_term())))
            self._isResult = True

    def clear(self):
        """Очистка вычисляемой строки."""
        self.term = "0"
