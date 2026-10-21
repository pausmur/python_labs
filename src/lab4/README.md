# Лабораторная №4
## Задание 1: реализация функций read_text и write_csv
### Функция read_text:
#### Читает файл в указанной кодировке (пользователь может вписать ее самостоятельно, но по умолчанию стоит utf-8 и возвращает как одну строку (хотя стоит считывать построчно). Если файл пустой, то выводит пустую строку
```python
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)
    return p.read_text(encoding=encoding)
```

### Функция write_csv:
#### Создает/перезаписывает CSV с разделителем ',', если передан header, то ставит его первой строкой и проверяет каждую строку в rows на равенство длин, иначе выдает ValueError
```python
from pathlib import Path
import csv
from typing import Iterable, Sequence

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)

    if rows:
        if not(header is None) and len(header) != len(rows[0]):
            raise ValueError('Разная длина')
        for x in rows:
            if len(x) != len(rows[0]):
                raise ValueError('Строки разной длины')
            
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
```
#### Тест-кейс
<img width="363" height="41" alt="lab4 1 text" src="https://github.com/user-attachments/assets/c3e76e45-6b5e-46b5-b8ee-ab6842204f51" />

<img width="181" height="102" alt="lab4 1 csv" src="https://github.com/user-attachments/assets/e4d2e040-a2f2-4654-840d-510e23e983dd" />

## Задание 2: скрипт, читающий файли с использованием ф-ций из задания 1
#### Скрипт читает файл, лежащий в data, нормализует текст из этого файла, токенизирует и считает частоты слов, после чего сохраняет report.csv с колонками word, count, а в консоль печатает краткое резюме. Если файл не найден или указана неверная кодировка, то через цикл except 'ловим' ошибку и принтим ее, после чего выходим из цикла try-except.
```python
import sys
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab4.io_txt_csv import read_text, write_csv

def text_report():
    try:
        text = read_text('data/lab04/input.txt', encoding='utf-8')
    except FileNotFoundError:
        print('Файл не был найден, попробуйте совершить ввод еще раз')
        sys.exit(1)
    except UnicodeDecodeError:
        print('Введен неверный тип расшифровки')
        sys.exit(1)

    normal_text = normalize(text)
    words = tokenize(normal_text)
    unique_words = count_freq(words)
    top5 = top_n(unique_words)

    print(f'Всего слов: {len(words)}')
    print(f'Уникальных слов: {len(unique_words)}')
    for i in top5:
        print(f'{i[0]}: {i[1]}')

    top_csv = sorted(unique_words.items(), key=lambda kv: (-kv[1], kv[0]))
    write_csv(top_csv, 'data/lab04/report.csv', header = ('word','count'))

if __name__ == '__main__':
    text_report()
```
#### Вывод при одном файле
<img width="670" height="132" alt="lab4 2 text" src="https://github.com/user-attachments/assets/8300176a-2732-4680-9a50-e0c6377cfa1e" />

<img width="160" height="73" alt="lab4 2 csv" src="https://github.com/user-attachments/assets/e1703d90-e4f9-43fd-8343-39b44494dbc3" />

#### Вывод при пустом файле (в report.csv остается только заголовок)
<img width="674" height="87" alt="lab4 2 text empty" src="https://github.com/user-attachments/assets/3ea65a88-b216-46fd-8283-5acb3b655940" />

<img width="161" height="49" alt="lab4 2 csv empty" src="https://github.com/user-attachments/assets/edd2b2eb-b9e0-4e00-80d5-ad3a08ceb48b" />

#### Вывод с кодировкой cp1251 (для вывода необходимо прописать в терминале py -m src.lab4.text_report --in data.lab04.input --encoding cp1251)
<img width="1037" height="113" alt="lab4 2 text cp1251" src="https://github.com/user-attachments/assets/c7fbd860-80cf-4f58-b617-acd8c78781e0" />

<img width="162" height="47" alt="lab4 2 csv cp1251" src="https://github.com/user-attachments/assets/cae2a7d2-72aa-41bf-a3d2-b4efa675fb08" />

### Краевые случаи
#### data/input.txt не существует - цикл try/except поймает ошибку и выведет ее в консоли
#### При пустом входе report.csv будет содержать только заголовок
#### При нестандартной кодировке необходимо указать в терминале --encode ... (где ... тип кодировки, пример у тест-кейса с кодировкой cp1251)
