import decimal

r = '13.14'
res = decimal.Decimal(r)

# print(res)
print(type(round(res,2)))

res = 123.123
print(type(round(res)))
print(decimal.Decimal(''))