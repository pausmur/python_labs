# Лабораторная №5
## Задание 1: реализация функций json_to_csv и csv_to_json
### Функция json_to_csv: проверяет файл на ошибки, читает его, после чего записывает словарь с заголовками в csv формате
```python
from pathlib import Path
import sys
import json
import csv

def json_to_csv(json_path: str, csv_path: str) -> None:
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if json_file is None: raise FileNotFoundError('Файл пустой')
    if json_file.suffix != '.json': raise ValueError('Неверный тип файла')
    if csv_file.suffix != '.csv': raise ValueError('Неверный тип файла')

    with open(json_file, "r", encoding="utf-8") as file:
            try:
                json_list = json.load(file)
            except json.JSONDecodeError:
                 print('Пустой файл')
                 sys.exit(1)

    if not isinstance(json_list,list): raise ValueError('Неверный тип данных')
    if not all(isinstance(list_item,dict) for list_item in json_list): raise ValueError('Неверный тип данных')

    fieldnames = dict()
    for i in json_list:
         for key in i.keys():
              fieldnames[key] = None

    with open(csv_file, 'w', newline = '', encoding = 'utf-8') as file:
         w = csv.DictWriter(file, fieldnames = fieldnames)
         w.writeheader()
         w.writerows(json_list)
```

### Функция csv_to_json: проверяет файл на ошибки, читает и записывает список данных в формате json (с кодировкой utf-8)
```python
def csv_to_json(csv_path: str, json_path: str) -> None:
    json_file = Path(json_path)
    csv_file = Path(csv_path)
    if json_file is None: raise FileNotFoundError('Пустой файл')
    if json_file.suffix != '.json': raise ValueError('Неверный тип файла')
    if  csv_file.suffix != '.csv': raise ValueError('Неверный тип файла')

    with open(csv_file, 'r', newline = '', encoding = 'utf-8') as file:
        DReader = csv.DictReader(file)
        if DReader.fieldnames == None: raise ValueError('Пустой заголовок')
        csv_list = list(DReader)

    if len(csv_list) == 0: raise ValueError('Пустой файл')
    with open(json_file, "w", encoding = "utf-8") as file:
        json.dump(csv_list, file, ensure_ascii = False, indent = 2)
```
### Вывод из терминала + результат в data/lab05/out:
#### py -m src.lab5.json_csv
<img width="373" height="167" alt="lab5_json_to_csv" src="https://github.com/user-attachments/assets/c815ccbd-a9b3-493a-84d4-1f6120b6ac0e" />
<img width="430" height="678" alt="lab5_csv_to_json" src="https://github.com/user-attachments/assets/8d09d7d5-759a-49e5-b3d3-2fd6b5b230f0" />

## Задание 2: реализация функции csv_to_xlsx
### Функция читает csv файл, проверяя на ошибки, после чего конвертирует его в формат xlsx
```python
import csv
from pathlib import Path
from openpyxl import Workbook

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)
    if csv_file is None: raise FileNotFoundError('Пустой файл')
    if csv_file.suffix != '.csv': raise ValueError('Неверный тип файла')
    if xlsx_file.suffix != '.xlsx': raise ValueError('Неверный тип файла')

    with open(csv_file, 'r', newline = '', encoding = 'utf-8') as file:
        file_reader = list(csv.reader(file))

    wb = Workbook()
    ws = wb.active
    ws.title = 'Sheet1'
    for row in file_reader:
        ws.append(row)
    for column in ws.columns:
        mx = 0
        lt = column[0].column_letter
        for item in column:
            if not(item.value) is None and len(str(item.value)) > mx: mx =  len(str(item.value))
        ws.column_dimensions[lt].width = max(mx, 8)
    wb.save(xlsx_file)
```
### Вывод из терминала + результат в data/lab05/out
#### py -m src.lab5.csv_xlsx
<img width="327" height="169" alt="lab5 csv_to_xlsx" src="https://github.com/user-attachments/assets/a24e410d-7f80-471d-9d3d-ff0a1a493df8" />