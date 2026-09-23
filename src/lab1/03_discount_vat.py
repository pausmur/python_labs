price_ = float(input('price = '))

if price_ <= 0: raise ValueError('Цена не может быть меньше или равна 0.') 

discount_ = float(input('discount = '))

if discount_ > 100: raise ValueError('Скидка не может быть больше 100%') 

vat_ = float(input('vat = '))

if vat_ > 100: raise ValueError('Процент налога не может быть больше 100%')

base = price_ * (1 - discount_/100)
vat_amount = base * (vat_/100)
total = base + vat_amount

print('База после скидки: ',f'{base:.2f}','₽')
print('НДС:',f'{vat_amount:.2f}','₽')
print('Итого к оплате:',f'{total:.2f}','₽')

