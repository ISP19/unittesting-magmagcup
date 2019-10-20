## Unit Testing Assignment

by Sirawich Direkwattanachai.

>>> [![Build Status](https://api.travis-ci.com/magmagcup/unittesting-magmagcup.svg?branch=master)](https://travis-ci.com/magmagcup/unittesting-magmagcup) [![codecov](https://codecov.io/gh/magmagcup/unittesting-magmagcup/branch/master/graph/badge.svg)](https://codecov.io/gh/magmagcup/unittesting-magmagcup)


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

"An integer is a whole number that can be either greater than 0, called positive, or less than 0, called negative. Zero is neither positive nor negative."
__Reference__: http://www.math.com/school/subject1/lessons/S1U1L10DP.html

Abbreviations in test case/result: 

__nan__: Not a number.

__inf__: Infinity.

## Constructor(init)

| Test case              |  Expected Result    |
|------------------------|---------------------|
| Positive int(> 0) as numerator |numerator = int,denominator = 1,spacial value = None             |
| Positive int(> 0) as numerator, Positive int(> 0) as denominator  |numerator = int,denominator = int,spacial value = None|
| Negative int(< 0) as numerator, Positive int(> 0) as denominator  |numerator = -int,denominator = int,spacial value = None|
| Positive int(> 0) as numerator, Negative int(< 0) as denominator  |numerator = -int,denominator = int,spacial value = None|
| Negative int(< 0) as numerator, Negative int(< 0) as denominator  |numerator = int,denominator = int,spacial value = None|
|Only input a denominator |  TypeError |
|Wrong argument type  |  TypeError |
|0 as denominator (positive numerator) | numerator = 1, denominator = 0,special value = inf|
|0 as denominator (negative numerator) | numerator = -1, denominator = 0,special value = -inf|
|0 as numerator  | numerator = 0, denominator = 1,special value = None|
|0 as numerator and denominator | numerator = 0, denominator = 0, special value = 'nan'
|Positive int as numerator, Negative 0 | numerator = 1, denominator = 0, special value = inf 
|Positive int as numerator, Positive 0 | numerator = 1, denominator = 0, special value = inf 

## Basetext (*__str__*)

| Test case              |   Expected Result    |
|------------------------|----------------------|
|Fraction with numerator > 0 (Denominator > 0)|numerator/denominator
|Fraction with numerator > 0  (Denominator = 1)| numerator
|Fraction with numerator < 0  (Denominator > 0)   |negative numerator/denominator                |
|Fraction with numerator < 0  (Denominator = 1 )  |negative numerator|
|Fraction with numerator < 0 (Denominator = 0) | -1/0
|Fraction with numerator > 0 (Denominator = 0) | 1/0
|Numerator = 0 (Denominator >0 or <0)| 0
|Numerator and Denominator = 0 | 0/0
|Numerator = 0 and Denominator != 0| 0

## Addition Operator(*__add__*)

| Test case              |   Expected Result    |
|------------------------|----------------------|
|Positive fraction(>0) + Positive fraction(>0) | Positive fraction     |
|Positive fraction(>0) + Negative fraction(<0) | Positive/Negative fraction (depend on the value of a negative fraction)|                   |
|Negative fraction(<0) + Negative fraction(<0) | Negative fraction
|Inf fraction + inf fraction or fraction + inf fraction | inf fraction|
|Inf fraction + Negative inf fraction | nan fraction|
|Negative inf fraction + Negative inf fraction or fraction + negative inf fraction| Negative inf fraction
|nan fraction + inf fraction or nan fraction + negative inf fraction | nan fraction|
|nan fraction + Positive fraction or nan fraction + negative fraction| nan fraction
|nan fraction + nan fraction | nan fraction

## Multiplication Operator(*__mul__*)

| Test case              |   Expected Result    |
|------------------------|----------------------|
|Positive fraction(>0) * Positive fraction(>0) | Positive fraction     |
|Positive fraction(>0) * Negative fraction(<0) | Negative fraction   |                   |
|Negative fraction(<0) * Negative fraction(<0) | Positive fraction
|Inf fraction * inf fraction or fraction * inf fraction | inf fraction|
|Inf fraction * Negative inf fraction |Negative inf fraction|
|Negative inf fraction * Negative inf fraction or negative fraction * negative inf fraction| Negative inf fraction
|nan fraction * inf fraction or nan fraction * negative inf fraction | nan fraction|
|nan fraction * Positive fraction or nan fraction * negative fraction| nan fraction
|nan fraction * nan fraction | nan fraction
|Fraction (=0) * inf/negative inf fraction | nan fraction
|Fraction (=0) * positive/negative fraction | Fraction(0)

## Subtraction Operator(*__sub__*)

| Test case              |   Expected Result    |
|------------------------|----------------------|
|Positive fraction(>0) - Positive fraction(>0) | Positive/Negative fraction (depend on the value of a negative fraction) |
|Positive fraction(>0) - Negative fraction(<0) | Positive fraction   |                   |
|Negative fraction(<0) - Negative fraction(<0) | Positive/Negative fraction (depend on the value of a negative fraction)||
|Negative fraction(<0) - Positive fraction(>0) | Negative fraction
|Inf fraction - inf fraction or Negative inf fraction - Negative inf fraction| nan fraction
|Inf fraction - fraction or fraction - negative inf fraction| inf fraction|
|Inf fraction - Negative inf fraction | Inf fraction|
|fraction - positive inf fraction or Negative inf fraction - fraction| Negative inf fraction
|nan fraction - inf fraction or nan fraction - negative inf fraction | nan fraction|
|nan fraction - Positive fraction or nan fraction - negative fraction| nan fraction
|nan fraction - nan fraction | nan fraction

## Greater than (*__gt__*)

| Test case              |   Expected Result    |
|------------------------|----------------------|
|2 Positive(>0) Fraction with same numerator but different denominator| return True if the base fraction have lower denominator value than the second one|
|2 Negative(<0) Fraction with same numerator but different denominator| return True if the base fraction have higher denominator value than the second one|
|Positive fraction and Negative fraction| if the base fraction is positive fraction, return True
|nan fraction, nan fraction| False|
|inf fraction, inf fraction or negative inf fraction, negative inf fraction| False|
|inf fraction, negative inf fraction| True|
|negative inf fraction, inf fraction| False|
|inf fraction,nan fraction| False|

## Negation Operator (*__neg__*)

| Test case              |   Expected Result    |
|------------------------|----------------------|
|Positive fraction| Negative fraction|
|Negative fraction| Positive fraction|
|inf fraction| Negative inf fraction|
|negative inf fraction| inf fraction|
|nan fraction| nan fraction|
|Fraction (0)| Fraction (0)|

## Equality Operator (*__eq__*)

| Test case              |   Expected Result    |
|------------------------|----------------------|
| Positive fraction,Same positive fraction without gcd division| True
| Positive fraction, Same fraction with negative sign | False
| Positive fraction, Another positive fraction without any resemblance to the first fraction| False|
| Negative fraction, Another negative fraction without any resemblance to the first fraction | False|
| Two fraction with the same numerator | False|
| Two fraction with the same denominator | False|
|Positive inf fraction, Positive inf fraction with numerator > 1 |True
| Fraction (0) , Fraction with numerator = 0,denominator != 0| True |
|Negative inf  fraction, Positive inf fraction | True|
