## Unit Testing Assignment

by Sirawich Direkwattanachai.


## Test Cases for unique

| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  Empty list         |
| one item               |  List with 1 item   |
| one item many times    |  List with 1 item   |
| 2 items, many times, many orders | 2 item list, items in same order  |
| many item, many times, many orders | List without duplicate item, in the same order
| Wrong argument type    | TypeError|
| Very large list        | List without duplicate item.


## Test Cases for Fraction
Test case for __init__,__add__,__mul__,__str__,__sub__,__gt__,__neq__,__eq__

##Constructor(init)
| Test case              |  Expected Result    |
|------------------------|---------------------|
| Input integer a as nominator |nominator = a,denominator = 1             |
| int a as nominator and int b as denominator  |nominator = a,denominator = b  |
|Only input denominator |  TypeError |
|Wrong argument type  |  TypeError |

##String(str)
| Test case              |   Expected Result    |
|------------------------|----------------------|
|                                               |
##