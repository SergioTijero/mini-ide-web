"""
lexer.py
Definición de tokens y analizador léxico usando PLY.
"""
import ply.lex as lex

# Lista de nombres de tokens
tokens = (
    'NUMBER',
    'ID',
    'PLUS','MINUS','TIMES','DIVIDE',
    'LPAREN','RPAREN',
    'COMMENT',
)

# Expresiones regulares para tokens simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

def t_COMMENT(t):
    r'//.*'
    # Los comentarios se ignoran pero se reconocen como tokens
    pass  # No se retorna nada, se ignora el comentario

def t_NUMBER(t):
    r'\d+'
    # Convierte cadenas a enteros
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t

# Ignorar espacios y tabs
t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    # En lugar de lanzar excepción, omite el carácter y continúa
    print(f"Carácter ignorado '{t.value[0]}' en línea {t.lineno}")
    t.lexer.skip(1)

# Construye el lexer
lexer = lex.lex()
