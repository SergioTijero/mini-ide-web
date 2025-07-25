
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMENT DIVIDE ID LPAREN MINUS NUMBER PLUS RPAREN TIMES\nexpression : expression PLUS term\n           | expression MINUS term\nexpression : term\nterm : term TIMES factor\n     | term DIVIDE factor\nterm : factorfactor : NUMBERfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'NUMBER':([0,5,6,7,8,9,],[4,4,4,4,4,4,]),'LPAREN':([0,5,6,7,8,9,],[5,5,5,5,5,5,]),'$end':([1,2,3,4,11,12,13,14,15,],[0,-3,-6,-7,-1,-2,-4,-5,-8,]),'PLUS':([1,2,3,4,10,11,12,13,14,15,],[6,-3,-6,-7,6,-1,-2,-4,-5,-8,]),'MINUS':([1,2,3,4,10,11,12,13,14,15,],[7,-3,-6,-7,7,-1,-2,-4,-5,-8,]),'RPAREN':([2,3,4,10,11,12,13,14,15,],[-3,-6,-7,15,-1,-2,-4,-5,-8,]),'TIMES':([2,3,4,11,12,13,14,15,],[8,-6,-7,8,8,-4,-5,-8,]),'DIVIDE':([2,3,4,11,12,13,14,15,],[9,-6,-7,9,9,-4,-5,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,5,],[1,10,]),'term':([0,5,6,7,],[2,2,11,12,]),'factor':([0,5,6,7,8,9,],[3,3,3,3,13,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS term','expression',3,'p_expression_binop','parser.py',21),
  ('expression -> expression MINUS term','expression',3,'p_expression_binop','parser.py',22),
  ('expression -> term','expression',1,'p_expression_term','parser.py',27),
  ('term -> term TIMES factor','term',3,'p_term_binop','parser.py',32),
  ('term -> term DIVIDE factor','term',3,'p_term_binop','parser.py',33),
  ('term -> factor','term',1,'p_term_factor','parser.py',38),
  ('factor -> NUMBER','factor',1,'p_factor_number','parser.py',42),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_group','parser.py',46),
]
