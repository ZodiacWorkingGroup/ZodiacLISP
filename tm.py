
# C:/Users/Owner/Desktop/Programming/Esolangs/ZodiacLISP\tm.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = 'C87B91A1109AC6C446071E4F111D73FE'
    
_lr_action_items = {'OPAREN':([0,1,2,3,4,5,6,7,8,9,10,],[1,1,-5,-7,-4,-6,1,1,-2,1,-1,]),'FLOAT':([0,1,2,3,4,5,6,7,8,9,10,],[2,2,-5,-7,-4,-6,2,2,-2,2,-1,]),'FUNC':([0,1,2,3,4,5,6,7,8,9,10,],[3,3,-5,-7,-4,-6,3,3,-2,3,-1,]),'$end':([2,3,4,5,6,8,9,10,],[-5,-7,-4,-6,0,-2,-3,-1,]),'INT':([0,1,2,3,4,5,6,7,8,9,10,],[4,4,-5,-7,-4,-6,4,4,-2,4,-1,]),'STR':([0,1,2,3,4,5,6,7,8,9,10,],[5,5,-5,-7,-4,-6,5,5,-2,5,-1,]),'CPAREN':([1,2,3,4,5,7,8,9,10,],[8,-5,-7,-4,-6,10,-2,-3,-1,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,1,6,7,9,],[6,7,9,9,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> OPAREN expression CPAREN','expression',3,'p_expression_s','parse.py',10),
  ('expression -> OPAREN CPAREN','expression',2,'p_expression_empty','parse.py',16),
  ('expression -> expression expression','expression',2,'p_expression_list','parse.py',22),
  ('expression -> INT','expression',1,'p_expression_unit','parse.py',29),
  ('expression -> FLOAT','expression',1,'p_expression_unit','parse.py',30),
  ('expression -> STR','expression',1,'p_expression_unit','parse.py',31),
  ('expression -> FUNC','expression',1,'p_expression_func','parse.py',38),
]
