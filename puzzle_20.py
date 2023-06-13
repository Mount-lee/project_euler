sum_dig = 0
factorial = 1
for i in range (1,101):
    factorial = i * factorial
factorial = [int(a) for a in str(factorial)]
for a in factorial:
    sum_dig += a

print(sum_dig)