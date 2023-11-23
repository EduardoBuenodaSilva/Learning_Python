#This module contains the main product

texts = (('1234,-24,0,9999999999999', 'Integer (Unlimited Size)'),
    ('1.23, 1., 3.14e-10, 4e210, 4.0e+210', 'Floating Point Numbers'),
    ('0o177, 0x9ff, 0b101010', 'Octal, hex and binary literal in 3.X'),
    ('0177, 0o177, 0x9ff, 0b101010', 'Octal, octal, hex and binary literal in 2.X'),
    ('3+4j, 3.0+4j, 3j', 'Complex number literals'),
    ("set('spam'), {1,2,3,4}", 'Sets: 2.X and 3.X construction forms'),
    ("Decimal('1.01), Fraction(1,3)", 'Decimal and Fracntion extension types'),
    ('bool(x), True, False', 'Boolean Type constrain'))
    

table = (('yield x', 'Generatpr function send protocol'),
         ('lambda args: expresssion', 'Anonymous function generation'),
         ('x if y else z', 'Ternary selection (x is evaluated only if y is True'),
         ('x or y','Logical OR'),
         ('x and y','Logical AND'),
         ('not x','Logical Negation'),
         ('x in y, x not in y','Membership (Iterables, sets)'),
         ('x < y, x <= y, x > y, x >= y','Magnituede comparison, set, subset an superset'),
         ('x==y, x!=y', 'Value equality operator'),
         ('x | y','Bitwise OR, set union'),
         ('x ^ y','Bitwise XOR, set symetric diference'),
         ('x & y','Bitwise AND, set intersection'),
         ('x << y, x >> y','Shift x left or right by y bits'),
         ('x + y','addition, concatenation'),
         ('x - y','subtraction, set difference'),
         ('x * y', 'Multiplication, repetition'),
         ('x % y','Remainder or Format'),
         ('x / y x // y','Division: True and floor'),
         ('-x, +x','Negation, identity'),
         ('~x','Bitwise NOT (Inversion)'),
         ('x**y','Power (exponentiation)'),
         ('x[i]','Indexing(sequence, mapping, others)'),
         ('x[i:j:k]','Slicing'),
         ('x(...)','call (function, method, class, other callable)'),
         ('x.attr','Atribute Rerefence'),
         ('(...)','Tuple, expression, generator expression'),
         ('[...]','List, List comprehensions'),
         ('{...}','Dictionaty, set, set and dictionaty comprehensions'),)


explanation ="""Operators lower in the table have higher precedence, and so bind more tightly in mi
xed expressions. Operators chained togheter with other have higher precedence
when they are lefter. Chaining a expression between parenthesis makes it have
the higher precedence, so the operator outside are evalueted after the parenthesis"""


