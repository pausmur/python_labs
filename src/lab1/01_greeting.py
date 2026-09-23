name_ = input('Имя: ')
age_ = int(input('Возраст: '))

if name_ in '0123456789.,': raise SyntaxError('Имя не может содержать числа.')
if age_ < 0: raise ValueError('Введите возраст больший нуля.')

print('Привет, ', name_, '!',' Через год тебе будет ',age_ + 1,sep='')

