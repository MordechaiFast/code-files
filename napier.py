"""A Program for making a table of Napierian logarithams and caculating with them."""
from decimal import Decimal


parts_in_unit = 10 ** 7
proportion = Decimal(parts_in_unit)
nlog = Decimal('10000000.0')
for n in range(135):
    print(f"{n:3}| {nlog:<.016}")
    nlog = nlog - nlog / proportion
