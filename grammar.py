import abc

# Abstract class for grammar's symbols
class Symbol(abc.ABC):

    def __init__(self, symbol):
        self.symbol = symbol

    def __str__(self):
        return self.symbol

    def __eq__(self, other):
        return self.symbol == other.symbol

    @abc.abstractmethod
    def is_terminal(self):
        return

# Terminal symbol (alphabet symbols)
class TerminalSymbol(Symbol):

    def __init__(self, symbol):
        super().__init__(symbol)

    def is_terminal(self):
        return True

# Non-terminal symbol (category)
class NonTerminalSymbol(Symbol):

    def __init__(self, symbol):
        super().__init__(symbol)

    def is_terminal(self):
        return False

# Chomsky production, that can assume the form A --> a or A --> BC
class ChomskyProduction:

    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

        # Assure valid productions
        assert len(self.rhs) == 1 or len(self.rhs) == 2

    def is_unit(self):
        return len(self.rhs) == 1

    def __str__(self):
        if self.is_unit():
            return str(self.lhs) + ' --> ' + str(self.rhs[0])
        else:
            return str(self.lhs) + ' --> ' + str(self.rhs[0]) + str(self.rhs[1])

# Context-free grammar <S, C, A, P> with:
#   S: initial symbol
#   C: list of non-terminal symbols (a.k.a. categories)
#   A: list of terminal symbols (a.k.a. alphabet)
#   P: list of productions in Chomsky normal form
class ContextFreeGrammar:

    def __init__(self, initial, categories, alphabet, productions):
        self.initial = initial
        self.categories = categories
        self.alphabet = alphabet
        self.productions = productions

        # Map categories to numbers (to help CYK indexing)
        self.map = {}
        for i, c in enumerate(self.categories):
            self.map[c.symbol] = i

    def __str__(self):
        string = ""
        for p in self.productions:
            string += str(p) + '\n'
        return string
