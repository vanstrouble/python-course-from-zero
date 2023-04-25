# NaN - Not a Number
import math
from decimal import Decimal

# Math module
a = float('NaN')
# print(f'a: {a}')
print(f'Es NaN: {math.isnan(a)}')

# Decimal module
a = Decimal('NaN')
# print(f'a: {a}')
print(f'Es NaN: {math.isnan(a)}')
