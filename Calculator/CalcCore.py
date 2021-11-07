from typing import Final


class CalcCore:

    OPERATION_CHARS: Final = ('+', '-', '*', '/')

    def __init__(self, term='0'):
        self._isResult = False
        self._result = '0'
        self.__term = term

    @property
    def text(self):
        if self._isResult:
            return self._result
        return self.term

    term = property()

    @term.getter
    def term(self):
        return self.__term

    @term.setter
    def term(self, value):
        self.__term = value
        if self._isResult:
            self._isResult = False

    def _getCalculatedTerm(self):
        if self.term[-1] in self.OPERATION_CHARS:
            return self.term[:-1]
        else:
            return self.term

    def addChar(self, char):
        if self._isResult:
            self.term = self._result
            self.addChar(char)
        elif char in self.OPERATION_CHARS:
            self.term = "%s%s" % (self._getCalculatedTerm(), char)
        else:
            if self.term == '0':
                self.term = char
            else:
                self.term = "%s%s" % (self.term, char)

    def calc(self):
        if not self._isResult:
            self._result = str(round(eval(self._getCalculatedTerm())))
            self._isResult = True

    def clear(self):
        self.term = "0"
