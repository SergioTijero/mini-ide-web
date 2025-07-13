"""
parser.py
Definición de la gramática y analizador sintáctico usando PLY.
"""
import ply.yacc as yacc
from lexer import tokens

class Node:
    """
    Nodo genérico para el AST.
    """
    def __init__(self, type_, children=None, value=None):
        self.type = type_
        self.children = children or []
        self.value = value

# Reglas de la gramática en BNF

def p_expression_binop(p):
    """
    expression : expression PLUS term
               | expression MINUS term
    """
    p[0] = Node('binop', [p[1], p[3]], p[2])

def p_expression_term(p):
    "expression : term"
    p[0] = p[1]

def p_term_binop(p):
    """
    term : term TIMES factor
         | term DIVIDE factor
    """
    p[0] = Node('binop', [p[1], p[3]], p[2])

def p_term_factor(p):
    "term : factor"
    p[0] = p[1]

def p_factor_number(p):
    "factor : NUMBER"
    p[0] = Node('number', value=p[1])

def p_factor_group(p):
    "factor : LPAREN expression RPAREN"
    p[0] = p[2]

def p_error(p):
    if p:
        raise SyntaxError(f"Error sintáctico en '{p.value}' (línea {p.lineno})")
    else:
        raise SyntaxError("Error sintáctico en EOF")

# Construye el parser
parser = yacc.yacc()
