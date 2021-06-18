from typing import Final

class CalcCore:


    OPERATION_CHARS: Final = ('+', '-', '*', '/')

    def __init__(self, term = '0'):
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

    def addChar(self, char):
        if self._isResult:
            self.term = self._result
            self.addChar(char)
        elif char in self.OPERATION_CHARS:
            if self.term[-1] in self.OPERATION_CHARS:
                self.term = "%s%s" % (self.term[:-1], char)
            else:
                self.term = "%s%s" % (self.term, char)
        else:
            if self.term == '0' or self._isResult:
                self.term = char
            else:
                self.term = "%s%s" % (self.term, char)

    def calc(self):
        if not self._isResult:
            if not self.term[-1] in self.OPERATION_CHARS:
                calc_text = self.term
            else:
                calc_text = self.term[:-1]
            self._result = str(round(eval(calc_text)))
            self._isResult = True

    def clear(self):
        self.term = "0"