from fractions import Fraction
from decimal import Decimal


print(Fraction(2, 3))
print(Fraction('2/3'))
print(Decimal(2/3))
print(Fraction(Decimal(0.666)))
print(Decimal(1.1))
print(Decimal('1.1'))
print(Fraction(Decimal(1.1)))
print(Fraction(Decimal('1.1')))
