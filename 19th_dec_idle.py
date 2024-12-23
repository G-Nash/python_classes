Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

5
5

5 + 2 + 1
8
8
8


5/0
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    5/0
ZeroDivisionError: division by zero
-5/0
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    -5/0
ZeroDivisionError: division by zero


x=1233455555
y=12312312412

x+y
13545767967
x-y
-11078856857
x*y
15186690139476848660
x/y
0.10018065768034216
x**y

========================================================== RESTART: Shell =========================================================

x/y
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x/y
NameError: name 'x' is not defined
x=12345
y=67890

x+y
80235
x-y
-55545
x*y
838102050
x/y
0.1818382677861246
x%y
12345
x//y
0
nash
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    nash
NameError: name 'nash' is not defined. Did you mean: 'hash'?
"nash"
'nash'
'nash'
'nash'
t='nash'
t
'nash'
type.t
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    type.t
AttributeError: type object 'type' has no attribute 't'
t.type
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    t.type
AttributeError: 'str' object has no attribute 'type'
type(t)
<class 'str'>



`nash`
SyntaxError: invalid syntax
len(t)
4
t[1]
'a'
t[1:2]
'a'
t[1:3]
'as'
t[:-1]
'nas'
'nas'
'nas'

id(t)
2467731773008
id(t[1])
140724010549512
a
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    a
NameError: name 'a' is not defined
a="some_string_for_sample"

a[::-1]
'elpmas_rof_gnirts_emos'
a[0:3}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
a[0:3]
'som'
a[0:2]
'so'
a
'some_string_for_sample'
>>> a[0:9]
'some_stri'
>>> a[0:14]
'some_string_fo'
>>> a[-2:-6]
''
>>> a[-1:-6:-1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> a[-1:-6:-1]
'elpma'
>>> 
>>> 1234+2
1236
>>> "1234"+3
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    "1234"+3
TypeError: can only concatenate str (not "int") to str
>>> "123"*4
'123123123123'
>>> 123*-1
-123
>>> "123"*-1
''
>>> "123"/2
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    "123"/2
TypeError: unsupported operand type(s) for /: 'str' and 'int'
>>> "nash "*5
'nash nash nash nash nash '
>>> "nash \n"*5
'nash \nnash \nnash \nnash \nnash \n'
>>> a[::2]
'sm_tigfrsml'
>>> a[::4]
's_ifsl'
