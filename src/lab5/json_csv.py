from pathlib import Path
import sys
import json
import csv

def json_to_csv(json_path: str, csv_path: str) -> None:
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if not(json_file.exists()): raise FileNotFoundError('Файл пустой')
    if json_file.suffix != '.json': raise ValueError('Неверный тип файла')
    if csv_file.suffix != '.csv': raise ValueError('Неверный тип файла')

    with open(json_file, "r", encoding="utf-8") as file:
            try:
                json_list = json.load(file)
            except json.JSONDecodeError:
                 print('Пустой файл или ошибка чтения(неверный формат)')
                 sys.exit(1)
    if json_list is None: raise FileNotFoundError('Пустой файл')
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

def csv_to_json(csv_path: str, json_path: str) -> None:
    json_file = Path(json_path)
    csv_file = Path(csv_path)
    if not(json_file.exists()): raise FileNotFoundError('Пустой файл')
    if json_file.suffix != '.json': raise ValueError('Неверный тип файла')
    if  csv_file.suffix != '.csv': raise ValueError('Неверный тип файла')

    with open(csv_file, 'r', newline = '', encoding = 'utf-8') as file:
        DReader = csv.DictReader(file)
        if DReader.fieldnames == None: raise ValueError('Пустой заголовок')
        csv_list = list(DReader)

    if len(csv_list) == 0: raise ValueError('Пустой файл')
    with open(json_file, "w", encoding = "utf-8") as file:
        json.dump(csv_list, file, ensure_ascii = False, indent = 2)

if __name__ == '__main__':
    json_to_csv('data/lab05/samples/people.json', 'data/lab05/out/people_from_json.csv')
    csv_to_json('data/lab05/samples/people.csv', 'data/lab05/out/people_from_csv.json')
         



               




