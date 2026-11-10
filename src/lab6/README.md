# Лабораторная №6
## Задание 1 - реализация функций cat и stats
### Функция cat выводит текст построчно или выводит его как нумерованный список, функция stats выводит топ-слов в тексте (по умолчанию 5)

```python
import argparse
from src.lib.io_helpers import read_text
from src.lib.text import normalize, tokenize,count_freq, top_n

def main():
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help='Файл для чтения')
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help = 'Файл для чтения')
    stats_parser.add_argument("--top", type=int, default=5, help = 'Количество слов для топа (по умолчанию 5)')

    args = parser.parse_args()

    if args.command == "cat":
        try:
            rows = read_text(args.input).splitlines()
        except FileNotFoundError:
            parser.error('Файл пуст или не найден')
        if args.n:
            for cnt in range(1, len(rows) + 1):
                print(f'{cnt} {rows[cnt - 1]}')
        else:
            for row in rows: print(row)

    elif args.command == "stats":
        try:
            text = read_text(args.input)
        except FileNotFoundError:
            parser.error('Файл пуст или не найден')
        if args.top <= 0: parser.error('Топ должен быть больше нуля')
        normal_text = normalize(text)
        tokens = tokenize(normal_text)
        unique_words = count_freq(tokens)
        top_words = top_n(unique_words, n = args.top)

        print(f'Всего слов: {len(tokens)}')
        print(f'Уникальных слов: {len(unique_words)}')
        print(f'Топ-{args.top} слов:')
        for words in top_words:
            print(f'{words[0]}: {words[1]}')

if __name__ == '__main__':
    main()
```
### Примеры вывода cat:
<img width="972" height="159" alt="cli_text cat" src="https://github.com/user-attachments/assets/e25166ab-532d-4791-afc7-2c129a39d777" />
<img width="969" height="156" alt="cli_text cat-n" src="https://github.com/user-attachments/assets/a08b64ad-2180-42b1-8e10-5ab0ea33c43a" />

#### Для запуска через консоль (построчно и пронумерованно):
```py -m src.lab6.cli_text cat --input data/lab06/text.txt```

```py -m src.lab6.cli_text cat --input data/lab06/text.txt -n```

### Примеры вывода stats:
<img width="964" height="199" alt="cli_text stats" src="https://github.com/user-attachments/assets/9dd1136d-4080-4082-ae6d-e25d3d022ad9" />
<img width="1036" height="228" alt="cli_text stats topn" src="https://github.com/user-attachments/assets/81881007-0285-4905-9b7e-94f538c2ce47" />

#### Для запуска через консоль (топ по умолчанию и выборочный)
```py -m src.lab6.cli_text stats --input data/lab06/text.txt```
```py -m src.lab6.cli_text stats --input data/lab06/text.txt --top 6```

### Вывод help
```py -m src.lab6.cli_text --help```
<img width="727" height="296" alt="cli_text help" src="https://github.com/user-attachments/assets/2816217d-60ed-4f53-a7f7-89be23c2b1a1" />

## Задание 2 - реализация конвертации разных типов файлов
```python
import argparse, json, csv
from src.lab5.json_csv import json_to_csv, csv_to_json
from src.lab5.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv", help = 'Переводит файл из json в csv')
    p1.add_argument("--in", dest="input", required=True)
    p1.add_argument("--out", dest="output", required=True)

    p2 = sub.add_parser("csv2json", help = 'Переводит файл из csv в json')
    p2.add_argument("--in", dest="input", required=True)
    p2.add_argument("--out", dest="output", required=True)

    p3 = sub.add_parser("csv2xlsx", help = 'Переводит файл из csv в xlsx')
    p3.add_argument("--in", dest="input", required=True)
    p3.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    try:
        if args.cmd == 'json2csv': json_to_csv(args.input, args.output)
        elif args.cmd == 'csv2json': csv_to_json(args.input, args.output)
        elif args.cmd == 'csv2xlsx': csv_to_xlsx(args.input, args.output)
    except FileNotFoundError as e:
        parser.error(str(e))
    except ValueError as e:
        parser.error(str(e))

if __name__ == '__main__':
    main()
```
### Примеры вывода:
<img width="291" height="173" alt="cli_convert json2csv" src="https://github.com/user-attachments/assets/f60862af-5e57-4b8f-8ad7-6afeb27804b0" />
<img width="326" height="677" alt="cli_convert csv2json" src="https://github.com/user-attachments/assets/0920b3bc-20c5-4413-b8df-26f09725a571" />
<img width="291" height="186" alt="cli_convert csv2xlsx" src="https://github.com/user-attachments/assets/8c20eeb6-dd81-4831-9993-4c267fc3ca1c" />

#### Для запуска через консоль:
```py -m src.lab6.cli_convert json2csv --in data/lab05/samples/people.json --out data/lab06/json2csv.csv```

```py -m src.lab6.cli_convert csv2json --in data/lab05/samples/people.csv --out data/lab06/csv2json.json```

```py -m src.lab6.cli_convert csv2xlsx --in data/lab05/samples/people.csv --out data/lab06/csv2xlsx.xlsx```

### Вывод help
```py -m src.lab6.cli_convert --help```
<img width="744" height="291" alt="help cli_convert" src="https://github.com/user-attachments/assets/dd25e67b-3a65-44e9-9485-38a430f90c80" />
