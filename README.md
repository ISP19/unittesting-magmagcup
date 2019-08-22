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

Test case for __init__,__string__,__add__,__mul__,__sub__,__gt__,__neq__,__eq__

## Constructor(init)

| Test case              |  Expected Result    |
|------------------------|---------------------|
| Positive int(> 0) as nominator |nominator = int,denominator = 1,spacial value = None             |
| Positive int(> 0) as nominator, Positive int(> 0) as denominator  |nominator = int,denominator = int,spacial value = None|
| Negative int(< 0) as nominator, Positive int(> 0) as denominator  |nominator = -int,denominator = int,spacial value = None|
| Positive int(> 0) as nominator, Negative int(< 0) as denominator  |nominator = -int,denominator = int,spacial value = None|
| Negative int(< 0) as nominator, Negative int(< 0) as denominator  |nominator = int,denominator = int,spacial value = None|
|Only input a denominator |  TypeError |
|Wrong argument type  |  TypeError |
|0 as denominator (positive nominator) | nominator = 1, denominator = 0,special value = inf|
|0 as denominator (negative nominator) | nominator = -1, denominator = 0,special value = -inf|
|0 as nominator  | nominator = 0, denominator = 1,special value = None|
|0 as nominator and denominator | nominator = 0, denominator = 0, special value = 'nan'
|Positive int as nominator, Negative 0 | nominator = 1, denominator = 0, special value = inf 
|Positive int as nominator, Positive 0 | nominator = 1, denominator = 0, special value = inf 

## Basetext (*__str__*)

| Test case              |   Expected Result    |
|------------------------|----------------------|
|Fraction with nominator > 0 (Denominator > 0)|nominator/denominator
|Fraction with nominator > 0  (Denominator = 1)| nominator
|Fraction with nominator < 0  (Denominator > 0)   | minus nominator/denominator                |
|Fraction with nominator < 0  (Denominator = 1 )  |minus nominator|
|Fraction with nominator < 0 (Denominator = 0) | -1/0
|Fraction with nominator > 0 (Denominator = 0) | 1/0
|Nominator and Denominator = 0 | 0/0
|Nominator = 0 and Denominator != 0| 0

## Addition Operator(*__add__*)

| Test case              |   Expected Result    |
|------------------------|----------------------|

## Multiplication Operator(*__mul__*)

| Test case              |   Expected Result    |
|------------------------|----------------------|

## Subtraction Operator(*__sub__*)

| Test case              |   Expected Result    |
|------------------------|----------------------|

## Greater than (*__gt__*)

| Test case              |   Expected Result    |
|------------------------|----------------------|

## Negation Operator (*__neg__*)

| Test case              |   Expected Result    |
|------------------------|----------------------|

## Equality (*__eq__*)

| Test case              |   Expected Result    |
|------------------------|----------------------|
