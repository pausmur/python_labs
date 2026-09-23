FIO = input('ФИО: ')
if FIO in '0123456789!@#$%^&*()_+={}[]":;<>,.?/№`~': raise TypeError('Имя не должно содержать лишние символы.')

letters_ = ''
FIO_No_Space = FIO.split()
count_space = len(FIO_No_Space) - 1
count_words = len(FIO_No_Space)

lenFIO = 0
for i in FIO_No_Space:
    lenFIO += len(i)

for i in FIO_No_Space:
    letters_ += i[0]

print('Инициалы: ', letters_.upper())
print('Длина (символов): ', lenFIO + count_space)


