# Infinite value handling
# Ways to use infinite values
import math
from decimal import Decimal

infinite_positive = float('inf')
# print(f'Positive infinite: {infinite_positive}')
# print(f'Is infinite: {math.isinf(infinite_positive)}')

infinite_negative = float('-inf')
# print(f'Negative infinite: {infinite_negative}')
# print(f'Is infinite: {math.isinf(infinite_negative)}')

# Math module
infinite_positive = math.inf
# print(f'Positive infinite: {infinite_positive}')
# print(f'Is infinite: {math.isinf(infinite_positive)}')

infinite_negative = -math.inf
# print(f'Negative infinite: {infinite_negative}')
# print(f'Is infinite: {math.isinf(infinite_negative)}')

# Decimal module
infinite_positive = Decimal('infinity')
# print(f'Positive infinite: {infinite_positive}')
# print(f'Is infinite: {math.isinf(infinite_positive)}')

infinite_negative = Decimal('-infinity')
print(f'Negative infinite: {infinite_negative}')
print(f'Is infinite: {math.isinf(infinite_negative)}')