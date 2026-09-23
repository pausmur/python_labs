minutes_ = int(input('Минуты:'))

if minutes_ <= 0: raise ValueError('Введите количество минут большее 0.')

def hours(n):
    if minutes_ >= 60:
        hours = minutes_ // 60
        mints_ = minutes_ - (hours * 60)
    if minutes_ <= 59:
        hours = 0
        mints_ = minutes_
    time_ = str(hours) + ':' + str(mints_)
    return time_
print(hours(minutes_))