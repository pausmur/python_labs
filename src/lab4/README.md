# Лабораторная №4
## Задание 1: реализация функций read_text и write_csv
### Функция read_text:
#### Читает файл в указанной кодировке и возвращает как одну строку (хотя стоит считывать построчно). Если файл пустой, то выводит пустую строку
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

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
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
![](./images/lab04/lab4.1.text.png)

![](./images/lab04/lab4.1.csv.png)

## Задание 2: скрипт, читающий файли с использованием ф-ций из задания 1
#### Скрипт читает файл, лежащий в data, нормализует текст из этого файла, токенизирует и считает частоты слов, после чего сохраняет report.csv с колонками word, count, а в консоль печатает краткое резюме
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
![](./images/lab04/lab4.2.text.png)

![](./images/lab04/lab4.2.text.png)

#### Вывод при пустом файле
![](./images/lab04/lab4.2.text.empty.png)

![](./images/lab04/lab4.2.csv.empty.png)

#### Вывод с кодировкой cp1251
![](./images/lab04/lab4.2.text.cp1251.png)

![](./images/lab04/lab4.2.text.cp1251.png)