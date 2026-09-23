a = input('a: ')
b = input('b: ')

a = float(a.replace(',','.'))
b = float(b.replace(',','.'))

summa = a + b
avg_ = (a + b)/2

print('sum=',f'{summa:.2f}','avg=',f'{avg_:.2f}')