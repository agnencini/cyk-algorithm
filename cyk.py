import sys
import numpy as np
from grammar import *
from utils import *

# Cocke–Younger–Kasami algorithm.
# Parse the derivations of a string given a CFG grammar in Chomsky normal form.
# Return the root of the derivation tree if the string is accepted, None if not.
def cyk(string, grammar):
    n = len(string)
    r = len(grammar.categories)

    nodes = np.ndarray((n + 1, n + 1, r), dtype=TreeNode)
    nodes.fill(None)

    # Parse productions in the form A --> a
    for i in range(1, n + 1):
        for pr in grammar.productions:
            if pr.is_unit() and pr.rhs[0] == string[i - 1]:
                nodes[1][i][grammar.map[pr.lhs.symbol]] = TreeNode(pr.lhs, TreeNode(pr.rhs[0], None, None), None)

    # Parse productions in the form A --> BC
    for l in range(2, n + 1):
        for s in range(1, n - l + 2):
            for p in range(1, l):
                for pr in grammar.productions:
                    if not pr.is_unit():
                        a = grammar.map[pr.lhs.symbol]
                        b = grammar.map[pr.rhs[0].symbol]
                        c = grammar.map[pr.rhs[1].symbol]

                        if nodes[p][s][b] != None and nodes[l - p][s + p][c] != None:
                            nodes[l][s][a] = TreeNode(pr.lhs, nodes[p][s][b], nodes[l - p][s + p][c])

    return nodes[n][1][grammar.map[grammar.initial.symbol]]

if __name__ == '__main__':

    # Load grammar definition from file (well-formed parenthesis in the example)
    cfg = load_grammar('well-formed-parenthesis-grammar')

    # A valid string for the language
    string = string_to_input('(()(()))')

    node = cyk(string, cfg)
