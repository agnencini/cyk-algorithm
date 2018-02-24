from grammar import *

# Derivation tree node. The grammar is in Chomsky normal form so the tree is
# guaranteed to be binary.
class TreeNode:

    def __init__(self, symbol, left, right):
        self.symbol = symbol
        self.left = left
        self.right = right

# Convert a list of symbols to a string
def input_to_string(terminal_symbols):
    string = ""
    for s in terminal_symbols:
        string += str(terminal_symbols)
    return string

# Convert a string to a list of symbol (CYK input)
def string_to_input(string):
    terminal_symbols = []
    for c in string:
        terminal_symbols.append(TerminalSymbol(c))
    return terminal_symbols

# Load a CNF grammar definition from file. The format is very simple:
# Line 0        : list of non-terminal symbols, comma separated
# Line 1        : list of terminal symbols, comma separated
# Line 2        : initial symbol
# Line [3, n)   : productions in the form A,a,null or A,B,C
#
# See the grammar file provided for an example.
def load_grammar(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            lines[i] = line.rstrip()

        categories = []
        for token in lines[0].split(','):
            categories.append(NonTerminalSymbol(token))

        alphabet = []
        for token in lines[1].split(','):
            alphabet.append(TerminalSymbol(token))

        initial = NonTerminalSymbol(lines[2])

        productions = []
        for i in range(3, len(lines)):
            split = lines[i].split(',')
            lhs = NonTerminalSymbol(split[0])
            rhs1 = split[1]
            rhs2 = split[2]

            if 'null' in rhs2:
                productions.append(ChomskyProduction(lhs,
                    [TerminalSymbol(rhs1)]))
            else:
                productions.append(ChomskyProduction(lhs,
                    [NonTerminalSymbol(rhs1), NonTerminalSymbol(rhs2)]))

        return ContextFreeGrammar(initial, categories, alphabet, productions)
