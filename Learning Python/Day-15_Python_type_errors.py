#Examples

#1 SyntaxError
print 'hello world'
#File "ThirtyDaysOfPython\Day-15_Python_type_errors.py", line 4
#    print 'hello world'
#    ^^^^^^^^^^^^^^^^^^^
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

#2 NameError
print(age)
#File "ThirtyDaysOfPython\Day-15_Python_type_errors.py", line 11, in <module>
#    print(age)
#          ^^^
#NameError: name 'age' is not defined

#3 IndexError
numbers = [1, 2, 3, 4, 5]
print(numbers[5])
#File "ThirtyDaysOfPython\Day-15_Python_type_errors.py", line 19, in <module>
#    print(numbers[5])
#          ~~~~~~~^^^
#IndexError: list index out of range

#4 ModuleNotFoundError
import maths
#File "ThirtyDaysOfPython\Day-15_Python_type_errors.py", line 26, in <module>
#    import maths
#ModuleNotFoundError: No module named 'maths'

#5 AttributeError
import math
math.PI
#File "ThirtyDaysOfPython\Day-15_Python_type_errors.py", line 33, in <module>
#    math.PI
#AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?

#6 KeyError
users = {'name':'Asab', 'age':250, 'country':'Finland'}
users['name']
#'Asab'
users['county']
#File "ThirtyDaysOfPython\Day-15_Python_type_errors.py", line 42, in <module>
#    users['county']
#    ~~~~~^^^^^^^^^^
#KeyError: 'county'

#7 TypeError
4 + '3'
#File "ThirtyDaysOfPython\Day-15_Python_type_errors.py", line 49, in <module>
#    4 + '3'
#    ~~^~~~~
#TypeError: unsupported operand type(s) for +: 'int' and 'str'

#8 ImportError
from math import power
#File "ThirtyDaysOfPython\Day-15_Python_type_errors.py", line 56, in <module>
#    from math import power
#ImportError: cannot import name 'power' from 'math' (unknown location)
#Correction: from math import pow

#9 ValueError
int('12a')
#File "ThirtyDaysOfPython\Day-15_Python_type_errors.py", line 63, in <module>
#    int('12a')
#    ~~~^^^^^^^
#ValueError: invalid literal for int() with base 10: '12a'

#10 ZeroDivisionError
1/0
#File "ThirtyDaysOfPython\Day-15_Python_type_errors.py", line 71, in <module>
#    1/0
#    ~^~
#ZeroDivisionError: division by zero

#The end